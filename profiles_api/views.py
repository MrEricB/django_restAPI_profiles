from django.http import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):
    """
    Test apiview
    """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """
        returns a list of apiview features as JSON
        """
        an_apiview = [
            'item 1',
            'item 2',
            'item 3'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """
        Create a hello message with name
        """

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
    def put(self, request, pk=None):
        """
        Handle updating an object
        """
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """
        Handle a partial update of an object
        """
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """
        Delete an object
        """
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """
    Test API ViewSet
    """
    serializer_class = serializers.HelloSerializer


    def list(self, resquest):
        """
        Return a hello message
        """
        a_viewset = [
            'item 1a',
            'item 2a',
            'item 3a'
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})
    
    def create(self, reqsuest):
        """
        Create a new hello message
        """
        serializer = self.serializer_class(data=reqsuest.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
            
    def retrieve(self, request, pk=None):
        """
        Handle getting an object by ID
        """
        return Response({'method': 'GET'})

    def update(self, request, pk=None):
        """
        handle updateing an object
        """
        return Response({'method': 'PUT'})

    def partial_update(self, request, pk=None):
        """
        handle updateing part of an object
        """
        return Response({'method': 'PATCH'})

    def destroy(self, request, pk=None):
        """
        handle deleting an object
        """
        return Response({'method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    Handle creating and updating profiles
    """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    
