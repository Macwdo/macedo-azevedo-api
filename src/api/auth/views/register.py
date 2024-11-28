from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.services import create_user


class RegisterApiView(APIView):
    class InputSerializer(serializers.Serializer):
        class PhoneSerializer(serializers.Serializer):
            number = serializers.CharField()
            ddi = serializers.CharField()
            ddd = serializers.CharField()

        first_name = serializers.CharField()
        last_name = serializers.CharField()
        email = serializers.EmailField()
        password = serializers.CharField()
        confirm_password = serializers.CharField()
        phone = PhoneSerializer()

        def validate_password(self, password):
            try:
                validate_password(password)
            except serializers.ValidationError as e:
                raise serializers.ValidationError(e.args[0]) from e

            return password

        def validate(self, data):
            if data["password"] != data["confirm_password"]:
                msg = "Passwords do not match"
                raise serializers.ValidationError(msg)

            return data

    def post(self, request):
        if request.user.is_authenticated:
            return Response(
                {"error": "You are already authenticated"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validated_data: dict = serializer.validated_data  # type: ignore

        create_user(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            password=validated_data["password"],
            phone_ddd=validated_data["phone"]["ddd"],
            phone_ddi=validated_data["phone"]["ddi"],
            phone_number=validated_data["phone"]["number"],
        )

        return Response(
            {"message": "User created"},
            status=status.HTTP_201_CREATED,
        )
