from rest_framework.serializers import ModelSerializer,SerializerMethodField

from rest_framework.response import Response
from rest_framework import status

from .models import Post,Scrap

class PostDetailSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

    

class ScrapSerializer(ModelSerializer):
    
    class Meta:
        model = Scrap
        fields = '__all__'

    def create(self, validated_data):
        scrap = Scrap.objects.create(**validated_data)
        scrap.user = self.context['request'].user
        scrap.save()
        return scrap
    

class ScrapPostListSerializer(ScrapSerializer):
    post_name = SerializerMethodField()


    def get_posts(self, obj):
        post_name = obj.post.name
        return post_name

    class Meta(ScrapSerializer.Meta):
        fields = ['post_name']