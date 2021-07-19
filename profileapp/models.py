from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') #이 프로파일과 유저 객체를  하나씩 연결해준다
    #객체가 사라졌을때의 정책 CASCADE
    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)

