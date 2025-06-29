from django import forms

from photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'


class PhotoAddForm(PhotoBaseForm):
    class Meta(PhotoBaseForm.Meta):
        exclude = ['date_of_publication']


class PhotoEditForm(PhotoBaseForm):
    class Meta(PhotoBaseForm.Meta):
        exclude = ['date_of_publication','photo']

        widgets = {
            'description':forms.TextInput(
                attrs={
                    'style':'padding 3px'
                }
            )
        }

        labels = {
            'tagged_pets':'Tag Pets'
        }

