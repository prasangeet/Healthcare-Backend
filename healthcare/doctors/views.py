from django.shortcuts import get_object_or_404
from django.db import IntegrityError

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Doctor
from .serializers import DoctorSerializer


# -------------------------
# CREATE doctor
# -------------------------
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_doctor(request):
    serializer = DoctorSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(
            {"success": False, "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        doctor = serializer.save()
    except IntegrityError:
        return Response(
            {"success": False, "error": "Database error"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    return Response(
        {"success": True, "data": DoctorSerializer(doctor).data},
        status=status.HTTP_201_CREATED,
    )


# -------------------------
# LIST doctors
# -------------------------
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def list_doctors(request):
    qs = Doctor.objects.all()
    data = DoctorSerializer(qs, many=True).data
    return Response({"success": True, "data": data})


# -------------------------
# GET doctor
# -------------------------
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_doctor(request, pk: int):
    doctor = get_object_or_404(Doctor, pk=pk)
    return Response({"success": True, "data": DoctorSerializer(doctor).data})


# -------------------------
# UPDATE doctor
# -------------------------
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_doctor(request, pk: int):
    doctor = get_object_or_404(Doctor, pk=pk)

    serializer = DoctorSerializer(doctor, data=request.data)

    if not serializer.is_valid():
        return Response(
            {"success": False, "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    serializer.save()

    return Response({"success": True, "data": serializer.data})


# -------------------------
# DELETE doctor
# -------------------------
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_doctor(request, pk: int):
    doctor = get_object_or_404(Doctor, pk=pk)
    doctor.delete()

    return Response(
        {"success": True, "message": "Doctor deleted"},
        status=status.HTTP_204_NO_CONTENT,
    )
