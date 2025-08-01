from django import forms

from common.mixins import ReadOnlyMixin
from pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'date_of_birth', 'personal_photo',)

        labels = {
            'name': 'Pet name',
            'date_of_birth': 'Date of birth',
            'personal_photo': 'Link to image'
        }

        widgets = {
            'date_of_birth': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),
            'personal_photo': forms.URLInput(
                attrs={
                    'placeholder': 'Link to image'
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Pet name'
                }
            )
        }


class PetCreateForm(PetBaseForm):
    pass



class PetEditForm(PetBaseForm):
    pass


class PetDeleteForm(ReadOnlyMixin,PetBaseForm):
    class Meta(PetBaseForm.Meta):
        fields = ('name', 'date_of_birth', 'personal_photo',)

        labels = {
            'name': 'Pet name',
            'date_of_birth': 'Date of birth',
            'personal_photo': 'Link to image'
        }
