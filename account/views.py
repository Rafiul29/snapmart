from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
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
            
            return Response({"error": "Incorrect username or password"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


class UserAccountLogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        print("USER",request.user)
        if not request.user.is_authenticated:  # Check if the user is authenticated
            return Response({"error": "User is not logged in"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            request.user.auth_token.delete()  # Delete the user's authentication token
            logout(request)  # Log out the user
            return Response({"success": "User Logout Successful"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
