from django.contrib.auth import authenticate
from django.db import IntegrityError

from django.db.models.fields import return_None
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from accounts.serializers import RegisterSerializer

from rest_framework_simplejwt.tokens import RefreshToken


@api_view(["POST"])
@permission_classes([AllowAny])
def register_view(request):
    serializer = RegisterSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(
            {
                "success": False,
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        user = serializer.save()

    except IntegrityError:
        return Response(
            {
                "success": False,
                "error": "User with this email already exists",
            },
            status=status.HTTP_409_CONFLICT,
        )

    except Exception as e:
        return Response(
            {
                "success": False,
                "error": "Internal server error",
                "detail": str(e),
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return Response(
        {
            "success": True,
            "message": "User registered successfully",
            "user_id": user.id,        # pyright: ignore
            "email": user.email,       # pyright: ignore
        },
        status=status.HTTP_201_CREATED,
    )

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response(
                {
                    "success": False,
                    "error": "Email and Password are required",
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    user = authenticate(request, email=email, password=password)

    if user is None:
        return Response(
            {
                "success": False,
                "error": "Invalid credentials",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )

    refresh = RefreshToken.for_user(user)

    return Response(
        {
            "success": True,
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user_id": user.id,
            "email": user.email
        },

    )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me_view(request):
    user = request.user

    if not user or not user.is_authenticated:
        return Response(
            {
                "success": False,
                "error": "Authetication required"
            },
            status=status.HTTP_401_UNAUTHORIZED,
        )

    return Response(
        {
            "success": True,
            "user": {
                "id": user.id,
                "email": user.email,
                "username": user.username,
                "date_joined": user.created_at
            }
        }
    )
