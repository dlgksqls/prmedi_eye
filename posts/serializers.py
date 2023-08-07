from rest_framework.serializers import ModelSerializer


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