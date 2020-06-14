from .models import Myfile
from rest_framework import serializers

class MyfileSeirializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Myfilefields = (
            'index', 'file_path', 'state', 'author'
        )