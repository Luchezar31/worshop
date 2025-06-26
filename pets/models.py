from django.db import models
from django.template.defaultfilters import slugify


class Pet(models.Model):
    name = models.CharField(
        max_length=30
    )
    personal_photo = models.URLField(
        max_length=5000,
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
        null=True,
        editable=False,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.pk}')

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
