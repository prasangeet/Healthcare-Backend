from django.urls import path
from .views import (
    create_patient,
    list_patients,
    get_patient,
    update_patient,
    delete_patient,
)

urlpatterns = [
    path("", list_patients),
    path("create/", create_patient),
    path("<int:pk>/", get_patient),
    path("<int:pk>/update/", update_patient),
    path("<int:pk>/delete/", delete_patient),
]
