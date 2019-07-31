#-*-coding:utf-8 -*-，
from blog.models import Post
from django.db import models


# Create your models here.
class Comment(models.Model):
    def __str__(self):
        return self.nickname
    Target = models.ForeignKey(Post,verbose_name="评论目标",on_delete=models.CASCADE)
    nickname = models.CharField(max_length=128,verbose_name="昵称")
    email= models.EmailField(verbose_name="邮箱")
    website = models.URLField(max_length=128,verbose_name="网址")
    content = models.TextField(blank=True)
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    class Meta:
        verbose_name = verbose_name_plural = "评论"

