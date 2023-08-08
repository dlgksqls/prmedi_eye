from django.shortcuts import render
from rest_framework import generics
from .serializers import UserModelSerializer
from .models import User

# Create your views here.

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    


