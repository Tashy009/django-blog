from .models import Comments
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'body')

    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'body': forms.Textarea(attrs={'class': 'form-control'}),
    }