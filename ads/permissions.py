from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to only allow admin users to edit objects.
    """

    def has_permission(self, request, view):
        # Allow read-only access to any user
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Allow write access only to admin users
        return request.user and request.user.is_staff
