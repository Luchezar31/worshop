from django import forms

from pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'


class PetCreateForm(PetBaseForm):
    class Meta(PetBaseForm.Meta):
        fields = ('name', 'date_of_birth', 'personal_photo',)

        labels = {
            'name': 'Pet name',
            'date_of_birth': 'Date of birth',
            'personal_photo': 'Link to image'
        }

        widgets = {
            'date_of_birth':forms.DateInput(
                attrs={
                    'type':'date'
                }
            ),
            'personal_photo':forms.URLInput(
                attrs={
                    'placeholder':'Link to image'
                }
            ),
            'name':forms.TextInput(
                attrs={
                    'placeholder':'Pet name'
                }
            )
        }



class PetEditForm(PetBaseForm):
    pass


class PetDeleteForm(PetBaseForm):
    pass
