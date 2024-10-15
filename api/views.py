from rest_framework import viewsets, mixins, permissions
from rest_framework import permissions
from rest_framework.permissions import IsAdminUser


from api.permissions import UserWithLawFirmPermission
from common.types import UserWithLawFirmRequest
from lawfirm.models import LawFirm, OwnedByLawFirm, OwnedByLawFirmQuerySet


class BaseGenericViewSet(viewsets.GenericViewSet):
    pass


class OwnedByLawFirmGenericViewSet(BaseGenericViewSet):
    request: UserWithLawFirmRequest
    permission_classes = [UserWithLawFirmPermission, IsAdminUser]

    def get_queryset(self):
        # TODO: Unit tests
        has_lawfirm_field = hasattr(self.queryset.model, "lawfirm")  # type: ignore
        assert has_lawfirm_field is True, "Model must have a 'lawfirm' field"

        current_lawfirm: LawFirm = self.request.user.current_lawfirm  # type: ignore
        queryset = super().get_queryset().filter_by_lawfirm(current_lawfirm)

        return queryset


class OwnedByLawFirmModelViewSet(
    OwnedByLawFirmGenericViewSet,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
):
    pass
