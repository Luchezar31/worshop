from django import forms
from common.models import Comment

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

        widgets = {
            'text':forms.Textarea(
                attrs={
                    'rows':10,
                    'cols':40,
                    'placeholder':'Add comment...'
                }
            )
        }

class SearchForm(forms.Form):
    text = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Search by pet name...'
            }
        )
    )