from rest_framework import permissions

class IsAccountAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user:
            return request.user.is_staff == True
        
        return False
