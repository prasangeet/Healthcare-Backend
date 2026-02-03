from rest_framework import serializers
from .models import PatientDoctorMapping


class MappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientDoctorMapping
        fields = "__all__"
        read_only_fields = ["id", "assigned_at"]

    def validate(self, data):
        request = self.context["request"]
        patient = data["patient"]

        if patient.created_by != request.user:
            raise serializers.ValidationError(
                "You can only map doctors to your own patients"
            )

        return data
