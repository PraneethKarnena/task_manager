from django.contrib.auth import get_user_model
from rest_framework import serializers

from dashboard.models import Project


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'pk')

class ProjectSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'