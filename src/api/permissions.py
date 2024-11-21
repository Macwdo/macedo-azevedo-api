from rest_framework import permissions


class UserWithLawFirmPermission(permissions.IsAuthenticated):
    def has_permission(self, request, view) -> bool:
        if not super().has_permission(request, view):
            return False

        return getattr(request.user, "current_lawfirm", None)
