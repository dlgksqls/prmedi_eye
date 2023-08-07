from django.shortcuts import render


from rest_framework.viewsets import generics,ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


from .serializers import PostDetailSerializer,ScrapSerializer,ScrapPostListSerializer
from .models import Post,Scrap


def AI_filter():
    '''
    대충 ai를 가지고 약 이름을 알아내는 모듈 함수를 대체하는 함수
    '''
    pass

def medi_selenium():
    '''
    대충 약 정보를 크롤링하는 모듈 함수를 대체하는 함수
    '''
    pass

class PostDetailView(APIView):
    permission_classes = [AllowAny]

    # 사진을 받고, 그 사진을 AI에 돌려서 결과를 받고, 그 약에 대한 post 객체가 있으면 그 객체를 반환
    # 만약없다면 post 객체를 만든 후 객체를 반환
    def get(self, request, *args, **kwargs):
        # ai works to get medi 
        medi_name = AI_filter(request.FILES['image'])
        try:
            serializer = self.get_serializer(Post.objects.get(id=medi_name))
        except Post.DoesNotExist:
            # dict 형태의 medi
            medi = medi_selenium(medi_name)
            serializer = self.get_serializer(Post.objects.create(
                name = medi['name'],
                image = medi['image'],
                medi_info = medi['medi_info'],
                url = medi['url'],
            ))
            serializer.save()
        return Response(serializer.data)



class ScarpView(ModelViewSet):
    serializer_class = ScrapSerializer
    queryset = Scrap.objects.all()
    permission_classes = [IsAuthenticated]


class ScrapPostView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, request):
        scrap_post = Scrap.objects.filter(user=request.user)
        return scrap_post
    
    def get(self, request):     
        serializer = ScrapPostListSerializer(self.get_object(request=request),many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)