from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.types import AuthenticatedUserRequest
from api.views import BaseApiView


class MeApiView(BaseApiView):
    permission_classes = [IsAuthenticated]

    def get(self, request: AuthenticatedUserRequest) -> Response:
        return Response(
            {
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
                "email": request.user.email,
            }
        )
