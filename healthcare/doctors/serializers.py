from rest_framework import serializers
from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = "__all__"
        read_only_fields = ["id", "created_at"]

    def validate_experience_years(self, value):
        if value < 0:
            raise serializers.ValidationError("Experience cannot be negative")
        if value > 80:
            raise serializers.ValidationError("Experience too large")
        return value
