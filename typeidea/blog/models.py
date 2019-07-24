#-*-coding:utf-8 -*-，
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    status_choice=[
        [0,"正常"],
        [1,"删除"]
    ]
    name = models.CharField(max_length=128,verbose_name="类别名称")
    status = models.IntegerField(default=1,choices=status_choice,verbose_name="状态")
    created_time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    is_nav=models.BooleanField(default=False,verbose_name="是否为导航")
    owner=models.ForeignKey(User,verbose_name="作者姓名",on_delete=models.CASCADE)
    class Meta:
        verbose_name = verbose_name_plural = '分类'
class Tag(models.Model):
    status_choice = [
        [0, "正常"],
        [1, "删除"]
    ]
    name = models.CharField(max_length=128, verbose_name="标签名称")
    status = models.IntegerField(default=1, choices=status_choice, verbose_name="状态")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    owner = models.ForeignKey(User, verbose_name="作者姓名",on_delete=models.CASCADE)
    class Meta:
        verbose_name = verbose_name_plural = "标签"
class Post(models.Model):
    status_choice = [
        [0, "正常"],
        [1, "删除"]
    ]
    title = models.CharField(max_length=128, verbose_name="标题")
    status = models.IntegerField(default=1, choices=status_choice,  verbose_name="状态")
    created_time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    category=models.ForeignKey(Category,verbose_name="类别名称",on_delete=models.CASCADE)
    tags= models.ManyToManyField(Tag,verbose_name="标签名称")
    owner= models.ForeignKey(User,verbose_name="作者",on_delete=models.CASCADE)
    description = models.TextField(blank=True,verbose_name="描述")
    content= models.TextField(verbose_name="内容")
    class Meta:
        verbose_name = verbose_name_plural = "文章"
        ordering = ['-id']