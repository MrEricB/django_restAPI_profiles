from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """
    Allow users to edit thier profile
    """

    def has_object_permission(self, request, view, obj):
        """"
        check if user is attempting to edit their profile
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """
    Allow user to edit there feeds
    """

    def has_object_permission(self, request, view, obj):
        """
        check if user is attempting to edit their feed
        """
        # print(obj.user_profile.id)
        # print(request.user.id)

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile.id == request.user.id
