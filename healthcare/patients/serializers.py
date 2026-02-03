from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = "__all__"
        read_only_fields = ["id", "created_by", "created_at", "updated_at"]

    def validate_age(self, value):
        if value <= 0:
            raise serializers.ValidationError("Age Must be positive")
        if value > 130:
            raise serializers.ValidationError("Age too large")
        return value
