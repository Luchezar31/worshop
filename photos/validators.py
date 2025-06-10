from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class PhotoSizeValidator:
    def __init__(self, photo_size, message=None):
        self.photo_size = photo_size
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if not value:
            self.message = f'Size of photo must be bigger than {self.photo_size}MB'

        self.__message = value

    def __call__(self, value):
        if value.size > self.photo_size * (1024**2):
            raise ValidationError(self.message)
