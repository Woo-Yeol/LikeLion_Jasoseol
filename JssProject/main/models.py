from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Jasoseol(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 오브젝트 즉 작성자가 없어졌을 때 작성자가 작성한 게시글 오브젝트도 없애준다.
