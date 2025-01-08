from rest_framework.permissions import BasePermission


class customer_permissions(BasePermission) :
    def has_object_permission(self, request, view, obj):
        request.user.is_authenticated == obj.user 