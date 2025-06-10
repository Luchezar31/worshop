from django.core.validators import MinLengthValidator
from django.db import models

from pets.models import Pet
from photos.validators import PhotoSizeValidator


class Photo(models.Model):
    photo = models.ImageField(
        validators=[
            PhotoSizeValidator(5)
        ],
        upload_to='files'
    )
    description = models.TextField(
        max_length=300,
        blank=True,
        null=True,
        validators=[
            MinLengthValidator(10),
        ]
    )
    location = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )
    tagged_pets = models.ManyToManyField(
        to=Pet,
        blank=True,
        related_name='photos'
    )
    date_of_publication = models.DateField(
        auto_now=True,
    )
