from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='article', null=True) #ForeignKey : 1대 다 로 연결 가능 / #on_delete=models.SET_NULL : 작성자 미상의 글로 남기겠다
    project = models.ForeignKey(Project, on_delete=models.SET_NULL,
                                related_name='article', null=True)

    title = models.CharField(max_length=200, null=True) #null = True : 사진만 올려도 된다~
    image = models.ImageField(upload_to='article/', null=True) #article폴더에 article관련 파일을 넣겠다
    content = models.TextField(null=True) #내용 안 쓸 수도 있지

    created_at = models.DateField(auto_now_add=True, null=True) #auto_now_add=True: DB내에서도 시간을 알아서 작성해주는 것

    like = models.IntegerField(default=0)