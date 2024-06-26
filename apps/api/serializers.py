from rest_framework import serializers

from apps.api.error_massages import (
    STATUS_NAME_LEN_ERROR_MESSAGE,
    CATEGORY_NAME_LEN_ERROR_MESSAGE,
)
from apps.todo.models import (
    Category,
    Status,
    Task,
    SubTask
)


class SubTaskPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['id', 'title', 'status']


class TaskInfoSerializer(serializers.ModelSerializer):
    subtasks = SubTaskPreviewSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'category',
            'status',
            'date_started',
            'deadline',
            'created_at',
            'subtasks'
        ]


class AllTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'creator',
            'category',
            'status',
            'date_started',
            'deadline',
            'created_at'
        ]


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

    def validate_name(self, value):
        if len(value) < 3 or len(value) > 30:
            raise serializers.ValidationError(
                STATUS_NAME_LEN_ERROR_MESSAGE
            )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def validate_name(self, value):
        if len(value) < 4 or len(value) > 25:
            raise serializers.ValidationError(
                CATEGORY_NAME_LEN_ERROR_MESSAGE
            )
