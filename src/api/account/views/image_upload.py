from rest_framework import serializers, status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.types import AuthenticatedUserRequest
from api.views import BaseApiView
from lawfirm.models import Account
from lawfirm.services import upload_account_image


class AccountImageUploadView(BaseApiView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]
    request: AuthenticatedUserRequest

    class InputSerializer(serializers.ModelSerializer):
        image = serializers.FileField()

        class Meta:
            model = Account
            fields = ["image"]

    def post(self, request, *args, **kwargs):
        account = request.user.account
        if not account:
            return Response(
                {"message": "Account not found"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data: dict = serializer.validated_data  # type: ignore

        upload_account_image(
            account=account,
            image=data["image"],
        )

        return Response(
            {"message": "Image uploaded successfully"},
            status=status.HTTP_200_OK,
        )
