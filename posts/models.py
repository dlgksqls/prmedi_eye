from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Post(models.Model):
    name = models.CharField(
        verbose_name='약 이름',
        max_length=30,
        unique=True
    )

    image = models.URLField(
        verbose_name='사진',
        default="",
    )
    
    medi_info = models.TextField(
        verbose_name='약물 정보',
    )

    url = models.URLField(
        verbose_name='약햑정보원 바로가기',
        default="",
    )

class Scrap(models.Model):

    post = models.ForeignKey(
        to='Post', 
        on_delete=models.CASCADE,
        related_name='scrap',
        )

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='scrap',
    )

