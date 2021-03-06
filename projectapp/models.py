from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='project/', null=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): #Project 클래스를 불러올 때
        return f'{self.name}'
