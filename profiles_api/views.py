from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView"""
        an_appview = [
            "uses http methods",
            "is similar to traditional django view",
            "gives you more control over app logic",
        ]

        return Response({
            'message': "Hello!",
            'an_appview': an_appview
        })

    def post(self, request):
        """create a hello message"""
        # passes the data from the request to the serializer obj
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"hello {name}"
            return Response({'message': message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class HelloViewSet(viewsets.ViewSet):
    """Test api viewset"""

    def list(self, request):
        a_viewset = [
            "element 1"
            "element 2"
            "element 3"
            "element 4"
        ]

        return Response({
            'message': "Hello!!",
            'a_viewset': a_viewset
        })


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """this allow us to view the login, by default is not rendered"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES