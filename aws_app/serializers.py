from rest_framework import serializers
from .models import Process

class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = "__all__"
        read_only_fields = ["id", "status", "result", "created_at"]