from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.types import AuthenticatedUserRequest
from api.views import BaseApiView


class MeApiView(BaseApiView):
    permission_classes = [IsAuthenticated]

    def get(self, request: AuthenticatedUserRequest) -> Response:
        user_image = request.user.account and request.user.account.image
        user_image_url = None
        if user_image:
            user_image_url = user_image.file.url

        return Response(
            {
                "code": request.user.code,
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
                "email": request.user.email,
                "image": user_image_url,
            },
        )
