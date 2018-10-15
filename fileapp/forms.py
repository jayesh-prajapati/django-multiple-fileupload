from django import forms
from .models import Fileup


class FileupForm(forms.ModelForm):
    class Meta:
        model = Fileup
        fields = ('file', )
        widgets = { 
            'file': forms.FileInput(attrs={'multiple': ''}),
        }  
