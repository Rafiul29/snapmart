from rest_framework.response import Response
from rest_framework.views import APIView

class Home(APIView):
    def get(self, request):
        return Response('Welcome to the server E-commerce Online Platform')
