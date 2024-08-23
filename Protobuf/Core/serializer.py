
from .models import SampleModel
from rest_framework import serializers

class SampleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleModel
        fields = ['id', 'name', 'description', 'data']


from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Project

User = get_user_model()

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'owner', 'is_default']

class UserSerializer(serializers.ModelSerializer):
    default_project_name = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'is_admin', 'default_project_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        default_project_name = validated_data.pop('default_project_name')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        # Create default project for this user
        Project.objects.create(
            name=default_project_name,
            owner=user,
            is_default=True
        )

        return user


class AdminSerializer(UserSerializer):
    
    def create(self, validated_data):
        validated_data['is_admin'] = True
        return super().create(validated_data)
