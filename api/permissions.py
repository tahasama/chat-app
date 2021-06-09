
from rest_framework import permissions #AllowAny, IsAuthenticated


class IsUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    def has_object_permission(self, request, view, obj):
        # print(obj.id)
        # print(request.user.id)
        return obj.id == request.user.id

class IsRoomer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    def has_object_permission(self, request, view, obj):
        if obj.owner.id == request.user.id:
            return True
        elif request.user in obj.joiners.all():
            return True
        return False