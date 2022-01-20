from rest_framework import serializers
from todo.models import Task, UserTaskProfile

class UserTaskProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTaskProfile
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    owner = UserTaskProfileSerializer(many=False)
    class Meta:
        model = Task
        fields = '__all__'


