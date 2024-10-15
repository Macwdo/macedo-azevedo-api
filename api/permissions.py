from rest_framework import permissions


class UserWithLawFirmPermission(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False

        current_lawfirm = getattr(request.user, "current_lawfirm", None)
        if not current_lawfirm:
            return False

        return True
