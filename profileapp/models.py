from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    # Accountapp과 1:1로 만들어줘야함
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')
    #on_delete = 게정이 삭제됐을 때 CASCADE(종속) 프로필도 동시에 삭제하겠다 라는 옵션 / SET_NULL 이라는 값으로도 가능
    #이미지,닉네임,메세지
    image = models.ImageField(upload_to='profile/', null=True)
    #경로 지정 옵션(Media root) / 이미지가 없다고 해도 괜찮다
    nickname = models.CharField(max_length=30, unique=True, null=True)
    #닉네임 길이 / 이 닉네임이 유일한(고유한)값을 가지도록 설정 /
    message = models.CharField(max_length=200, null=True)
#migration 을 해줘야 한다!!!
#터미널에서 pip install pillow를 해줬고
#python manage.py makemigrations 를 입력하면 폴더를 생성해주고
#python manage.py migrate 를 입려해줘야한다.
