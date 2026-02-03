from django.shortcuts import get_object_or_404
from django.db import IntegrityError

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import PatientDoctorMapping
from .serializers import MappingSerializer
from patients.models import Patient


# -------------------------
# CREATE mapping
# -------------------------
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_mapping(request):
    serializer = MappingSerializer(
        data=request.data,
        context={"request": request}
    )

    if not serializer.is_valid():
        return Response(
            {"success": False, "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        mapping = serializer.save()

    except IntegrityError:
        return Response(
            {"success": False, "error": "Mapping already exists"},
            status=status.HTTP_409_CONFLICT,
        )

    return Response(
        {"success": True, "data": MappingSerializer(mapping).data},
        status=status.HTTP_201_CREATED,
    )


# -------------------------
# LIST all mappings (my patients only)
# -------------------------
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def list_mappings(request):
    qs = PatientDoctorMapping.objects.filter(
        patient__created_by=request.user
    )

    data = MappingSerializer(qs, many=True).data
    return Response({"success": True, "data": data})


# -------------------------
# GET doctors for patient
# -------------------------
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def mappings_for_patient(request, patient_id: int):
    patient = get_object_or_404(
        Patient,
        pk=patient_id,
        created_by=request.user
    )

    qs = PatientDoctorMapping.objects.filter(patient=patient)
    data = MappingSerializer(qs, many=True).data

    return Response({"success": True, "data": data})


# -------------------------
# DELETE mapping
# -------------------------
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_mapping(request, pk: int):
    mapping = get_object_or_404(
        PatientDoctorMapping,
        pk=pk,
        patient__created_by=request.user
    )

    mapping.delete()

    return Response(
        {"success": True, "message": "Mapping removed"},
        status=status.HTTP_204_NO_CONTENT,
    )
