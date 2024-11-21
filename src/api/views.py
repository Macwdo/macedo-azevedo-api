from typing import TYPE_CHECKING

from rest_framework import mixins, views, viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.permissions import UserWithLawFirmPermission
from api.types import UserWithLawFirmRequest

if TYPE_CHECKING:
    from lawfirm.models import LawFirm


class BaseGenericViewSet(viewsets.GenericViewSet):
    pass


class BaseApiView(views.APIView):
    authentication_classes = [JWTAuthentication]


class OwnedByLawFirmGenericViewSet(BaseGenericViewSet):
    request: UserWithLawFirmRequest
    permission_classes = [UserWithLawFirmPermission, IsAdminUser]

    def get_queryset(self):
        has_lawfirm_field = hasattr(self.queryset.model, "lawfirm")  # type: ignore
        assert has_lawfirm_field is True, "Model must have a 'lawfirm' field"

        current_lawfirm: LawFirm = self.request.user.current_lawfirm  # type: ignore
        return super().get_queryset().filter_by_lawfirm(current_lawfirm)


class OwnedByLawFirmModelViewSet(
    OwnedByLawFirmGenericViewSet,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
):
    pass
