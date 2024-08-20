
from .models import SampleModel
from rest_framework import serializers

class SampleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleModel
        fields = ['id', 'name', 'description', 'data']
