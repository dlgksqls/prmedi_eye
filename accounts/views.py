from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,AllowAny

from .serializers import (UserModelSerializer,UserSignupSerializer,DiseaseMediSerializer,
MedicineSerializer, AllergyMediSerializer)
from .models import User,medicine

# Create your views here.

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    

class UserSignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer


class UserSigninView():
    pass





class UserDiseaseMediView(generics.ListAPIView):
    serializer_class = DiseaseMediSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return user.disease.all()
    
class UserAllergyMediView(generics.ListAPIView):
    serializer_class = AllergyMediSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return user.allergy.all()
    
# 유저의 약 리스트를 보여주는 뷰
class UserMediListView(generics.ListAPIView):

    serializer_class = MedicineSerializer   
    def get_queryset(self):
        return medicine.objects.filter(user=self.request.user)
    
class UserMediViewSet(ModelViewSet):

    serializer_class = MedicineSerializer
    queryset = medicine.objects.all()
    