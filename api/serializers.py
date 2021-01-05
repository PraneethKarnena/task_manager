from django.contrib.auth import get_user_model
from rest_framework import serializers

from dashboard.models import Project, Task, SubTask


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'pk')


class SubTaskSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(many=False, read_only=True)
    assignee = UserSerializer(many=False)
    
    class Meta:
        model = SubTask
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(many=False, read_only=True)
    assignee = UserSerializer(many=False)

    class Meta:
        model = Task
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(many=False, read_only=True)
    tasks = TaskSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'