from django.db import models
from django.conf import settings

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=20)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='user_image',blank=True,null=True)
    post_hit = models.PositiveIntegerField(default=0)

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField()
# Create your models here.
