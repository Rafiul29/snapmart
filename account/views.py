from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token

from .serializers import UserAccountRegistrationSerializer, UserAccountLoginSerializer


class UserAccountRegistrationView(APIView):
    def post(self, request):
        serializer = UserAccountRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAccountLoginView(APIView):
    def post(self,request):
        serializer = UserAccountLoginSerializer(data=request.data)
        if serializer.is_valid():
            username=serializer.validated_data['username']
            password= serializer.validated_data['password']

            user= authenticate(username=username,password=password)

            if user:
                token, _ = Token.objects.get_or_create(user=user)
               
                login(request,user)
                return Response({
                'token' : token.key,                 
                'user' :{
                "user_id":user.id,
                'username':user.username,
                'email':user.email,
                'role':user.role
            }}, status=status.HTTP_200_OK)
            
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAccountLogoutView(APIView):
   def get(self,request):
      request.user.auth_token.delete()
      logout(request)
      return Response({"success": "User Logout Successfull"}, status=status.HTTP_200_OK)


#   {
# "username":"rafiul",
# "email":"rafiul123@gmail.com",
# "first_name":"Rafiul",
# "last_name":"Islam",
# "password":"Rafi@#12",
# "confirm_password":"Rafi@#12",
# "role":"admin"
# }

# {
# "username":"rafiul",
# "password":"Rafi@#12"
# }
