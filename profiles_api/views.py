from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """
    Test apiview
    """

    def get(self, request, format=None):
        """
        returns a list of apiview features
        """
        an_apiview = [
            'item 1',
            'item 2',
            'item 3'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})