from django import forms
from .models import Myfile

class MyfileForm(forms.ModelForm):
    class Meta:
        model = Myfile
        fields = ['index', 'file_path', 'state']
        labels = {
            'index': 'index',
            'file_path': 'file_path',
            'state': 'state',
        }
