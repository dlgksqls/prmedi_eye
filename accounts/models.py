from django.db import models
from django.contrib.auth.models import PermissionsMixin, UserManager as DjangoUserManager
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
# Create your models here.

# user = get_user_model()
class UserManager(DjangoUserManager): #장고 모델이 디비로 쿼리를 날릴 때 제공해주는 인터페이스 슈퍼유저인지 일반유저인지?
    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('이메일은 필수 값입니다.')
        
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password) #비밂번호는 나만 알아야함.. 데이터베이스에 해싱해서 들어감
        user.save() 
    
    def create_user(self, username, email=None, password=None, **extra_fields): #일반 유저
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(username,email,password,**extra_fields)
    
    def create_superuser(self, username, email, password,**extra_fields): #슈퍼 유저
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(username,email,password,**extra_fields)
    


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(verbose_name='username', max_length=10)
    password = models.CharField(verbose_name='password',max_length=15)
    age = models.IntegerField(verbose_name='age',default=0)
    phone = models.CharField(verbose_name='phone', max_length=15)
    email = models.EmailField(verbose_name='email',unique=True)
    pregnancy = models.BooleanField(verbose_name='gregnancy',default=False)
    
    is_staff = models.BooleanField(_("staff status"), default=False)
    is_active = models.BooleanField(_("active"), default=True)

    objects = UserManager()
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
        


class disease(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True, related_name='disease')
    name = models.CharField(verbose_name='disease_name',max_length=15)


class allergy(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True, related_name='allergy')
    name = models.CharField(verbose_name='allergy_name',max_length=15)


class medicine(models.Model):
    order = models.IntegerField(verbose_name='number',default=0,null=True)
    name = models.TextField(verbose_name='medicine_name',null=True,default='')
    classification = models.TextField(verbose_name='medi_classification',null=True,default='')
    Ingredients_amount = models.TextField(verbose_name='Ingredients_amount',default='',null=True)
    efficacy = models.TextField(verbose_name='efficacy',null=True)
    infomation = models.TextField(verbose_name='infomation',default='',null=True)
    warning = models.TextField(verbose_name='warning',null=True,default='')
    storage = models.TextField(verbose_name='storage',null=True,default='')
    doping = models.TextField(verbose_name='doping',null=True,default='')
    usage = models.TextField(verbose_name='usage',null=True,default='')
    user = models.ForeignKey (User, on_delete=models.CASCADE, null=True, blank=True, related_name='medicine') 

    disease = models.ForeignKey(
        to = 'disease',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='disease_medi',
        )
    
    allergy = models.ForeignKey(
        to = 'allergy',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='allergy_medi',
    )
