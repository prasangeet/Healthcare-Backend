from django.db import models
from django.core.exceptions import ValidationError

from patients.models import Patient
from doctors.models import Doctor


class PatientDoctorMapping(models.Model):

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="doctor_links"
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="patient_links"
    )

    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["patient", "doctor"],
                name="unique_patient_doctor"
            )
        ]

    def clean(self):
        if self.patient_id == self.doctor_id:
            raise ValidationError("Invalid mapping")

    def __str__(self):
        return f"{self.patient_id} → {self.doctor_id}"
