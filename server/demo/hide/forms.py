from django import forms
from .models import Myfile, NetworkState

class MyfileForm(forms.ModelForm):
    class Meta:
        model = Myfile
        fields = ['file_path', 'state']
        labels = {
            'file_path': 'file_path',
            'state': 'state',
        }

class NetworkStateForm(forms.ModelForm):
    from rest_framework.permissions import IsAuthenticated
    permission_classes = (IsAuthenticated,)

    class Meta:
        model = NetworkState
        fields = ['network_state']
        labels = {
            'network_state': 'network_state',
        }
