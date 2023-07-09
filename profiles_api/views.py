from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

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
