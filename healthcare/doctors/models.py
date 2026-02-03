from django.db import models
from django.core.exceptions import ValidationError


class Doctor(models.Model):

    name = models.CharField(max_length=120)
    specialization = models.CharField(max_length=120)
    experience_years = models.PositiveIntegerField()
    hospital = models.CharField(max_length=150, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    # -------------------
    # model validation
    # -------------------
    def clean(self):
        if self.experience_years > 80:
            raise ValidationError("Experience years invalid")

    def __str__(self):
        return f"Dr. {self.name} — {self.specialization}"
