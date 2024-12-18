from django.shortcuts import render

# Create your views here.

from rest_framework import status, permissions, views, generics, parsers, response

from .models import UserProfile

from .serializers import UserProfileSerializer
from rest_framework import status, permissions, views, response
from .models import UserProfile
from .serializers import UserProfileSerializer

# class UserProfileView(views.APIView):
#     permission_classes = [permissions.IsAuthenticated]  # Ensure only authenticated users can access

#     def get(self, request, *args, **kwargs):
#         # Get the authenticated user's profile
#         user = request.user
#         try:
#             # Assuming the user has a related UserProfile
#             profile = user.profile  # This assumes a one-to-one relationship between User and UserProfile
#             serializer = UserProfileSerializer(profile)
#             return response.Response(serializer.data)
#         except UserProfile.DoesNotExist:
#             return response.Response({"error": "Profile not found."}, status=status.HTTP_404_NOT_FOUND)

#     def put(self, request, *args, **kwargs):
#         # Update the authenticated user's profile
#         user = request.user
#         try:
#             # Get the existing profile or create a new one if it doesn't exist
#             profile = user.profile  # Assuming a one-to-one relationship

#             # Pass the profile instance and the data to the serializer
#             serializer = UserProfileSerializer(profile, data=request.data)

#             if serializer.is_valid():
#                 serializer.save()
#                 return response.Response(serializer.data)
#             return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         except UserProfile.DoesNotExist:
#             return response.Response({"error": "Profile not found."}, status=status.HTTP_404_NOT_FOUND)



class UserProfileView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]  # Ensure only authenticated users can access

    def get(self, request, *args, **kwargs):
        # Get the authenticated user
        user = request.user
        serializer = UserProfileSerializer(user)
        return response.Response(serializer.data)

    def put(self, request, *args, **kwargs):
        # Update the authenticated user's profile
        user = request.user
        serializer = UserProfileSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserProfileUpdateView(views.APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = UserProfileSerializer
#     parser_classes = [parsers.FormParser, parsers.MultiPartParser]

#     def get(self, request, id):
#         profile = Profile.objects.get(id=id)
#         serializer = UserProfileSerializer(profile)
#         return response.Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, id):
#         profile = Profile.objects.get(id=id)
#         serializer = UserProfileSerializer(profile, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return response.Response(serializer.data, status=status.HTTP_200_OK)
    
    