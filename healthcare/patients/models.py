from django.db import models
from django.conf import settings
from django.forms import ValidationError

from accounts.models import User

# Create your models here.

class Patient(models.Model):
    
    class Gender(models.TextChoices):
        MALE='male', 'Male',
        FEMALE="female", "Female",
        OTHER = "other", "Other"

    created_by = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            related_name="patients"
        )

    name = models.CharField(max_length=120)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=Gender.choices)
    diagnosis = models.TextField(blank=True)

    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)


    def clean(self):
        if self.age > 130:
            raise ValidationError("Age seems invalid")

    def __str__(self):
        return f"{self.name} ({self.age})"
