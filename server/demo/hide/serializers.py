from .models import HideList
from rest_framework import serializers

class HideListSeirializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HideListfields = (
            'index', 'file_path', 'state', 'priority'
        )