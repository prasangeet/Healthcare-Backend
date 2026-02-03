from django.urls import path
from .views import (
    create_doctor,
    list_doctors,
    get_doctor,
    update_doctor,
    delete_doctor,
)

urlpatterns = [
    path("", list_doctors),
    path("create/", create_doctor),
    path("<int:pk>/", get_doctor),
    path("<int:pk>/update/", update_doctor),
    path("<int:pk>/delete/", delete_doctor),
]
