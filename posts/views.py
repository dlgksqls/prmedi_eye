from django.shortcuts import render


from rest_framework.viewsets import generics,ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
# Create your views here.


from .serializers import PostDetailSerializer,ScrapSerializer
from .models import Post,Scrap

class PostDetailView(generics.RetrieveAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    permission_classes = [AllowAny]

class ScarpView(ModelViewSet):
    serializer_class = ScrapSerializer
    queryset = Scrap.objects.all()
    permission_classes = [IsAuthenticated]