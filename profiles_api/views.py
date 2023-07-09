from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


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
