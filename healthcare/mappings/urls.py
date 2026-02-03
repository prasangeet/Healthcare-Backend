from django.urls import path
from .views import (
    create_mapping,
    list_mappings,
    mappings_for_patient,
    delete_mapping,
)

urlpatterns = [
    path("", list_mappings),
    path("create/", create_mapping),
    path("patient/<int:patient_id>/", mappings_for_patient),
    path("<int:pk>/delete/", delete_mapping),
]
