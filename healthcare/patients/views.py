from django.shortcuts import get_object_or_404
from django.db import IntegrityError

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Patient
from .serializers import PatientSerializer


# -------------------------
# CREATE patient
# -------------------------
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_patient(request):
    serializer = PatientSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(
            {"success": False, "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        patient = serializer.save(created_by=request.user)

    except IntegrityError:
        return Response(
            {"success": False, "error": "Database error"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    return Response(
        {"success": True, "data": PatientSerializer(patient).data},
        status=status.HTTP_201_CREATED,
    )


# -------------------------
# LIST my patients
# -------------------------
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def list_patients(request):
    qs = Patient.objects.filter(created_by=request.user)
    data = PatientSerializer(qs, many=True).data

    return Response({"success": True, "data": data})


# -------------------------
# GET one patient
# -------------------------
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_patient(request, pk: int):
    patient = get_object_or_404(
        Patient, pk=pk, created_by=request.user
    )

    return Response(
        {"success": True, "data": PatientSerializer(patient).data}
    )


# -------------------------
# UPDATE patient
# -------------------------
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_patient(request, pk: int):
    patient = get_object_or_404(
        Patient, pk=pk, created_by=request.user
    )

    serializer = PatientSerializer(
        patient, data=request.data, partial=False
    )

    if not serializer.is_valid():
        return Response(
            {"success": False, "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    serializer.save()

    return Response(
        {"success": True, "data": serializer.data}
    )


# -------------------------
# DELETE patient
# -------------------------
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_patient(request, pk: int):
    patient = get_object_or_404(
        Patient, pk=pk, created_by=request.user
    )

    patient.delete()

    return Response(
        {"success": True, "message": "Patient deleted"},
        status=status.HTTP_204_NO_CONTENT,
    )
