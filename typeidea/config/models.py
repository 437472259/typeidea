#-*-coding:utf-8 -*-，

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Sidebar(models.Model):
    CHOICE_ITEM=(
        (0,"删除"),
        (1,"正常")
    )
    SIDE_TYPE=(
        (1,"HTML"),
        (2,"最新文章"),
        (3, "最热文章"),
        (4, "最近评论"),
    )
    title = models.CharField(max_length=1024,verbose_name="名称")
    type = models.IntegerField(default=1,choices=SIDE_TYPE,verbose_name="类型")
    status = models.IntegerField(default=1,choices=CHOICE_ITEM,verbose_name="状态")
    content = models.TextField(verbose_name="内容",blank=True,help_text="如果设置的不是html，可为空")
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="创建日期")
    owner = models.ForeignKey(User,verbose_name="作者",on_delete=models.CASCADE)
    class Meta:
        verbose_name = verbose_name_plural = "侧边栏"


class Link(models.Model):
    CHOICE_ITEM=(
        (0,"删除"),
        (1,"正常状态")
    )
    title = models.CharField(max_length=512,verbose_name="标题")
    href = models.URLField(verbose_name="连接地址")
    status = models.IntegerField(default=1,choices=CHOICE_ITEM,verbose_name="状态")
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    weight = models.IntegerField(default=1,choices=zip(range(1,6),range(1,6)),verbose_name="重量",help_text="权重高展示顺序靠前")
    owner = models.ForeignKey(User,verbose_name="作者",on_delete=models.CASCADE)
    class Meta:
        verbose_name=verbose_name_plural = "链接"
