#-*-coding:utf-8 -*-，

from django.db import models
from django.contrib.auth.models import User
from django.template.loader import render_to_string

# Create your models here.
class Sidebar(models.Model):
    def __str__(self):
        return self.title
    DISPLAY_HTML=1
    DISPLAY_LATEST=2
    DISPLAY_HOT=3
    DISPLAY_COMMENT=4
    STATUS_NORMAL = 1;
    STATUS_DELETE = 0;
    STATUS_ITEM = (
        (STATUS_NORMAL, "正常"),
        (STATUS_DELETE, "删除")
    )
    SIDE_TYPE=(
        (DISPLAY_HTML,"HTML"),
        (DISPLAY_LATEST,"最新文章"),
        (DISPLAY_HOT, "最热文章"),
        (DISPLAY_COMMENT, "最近评论"),
    )
    title = models.CharField(max_length=1024,verbose_name="名称")
    type = models.IntegerField(default=DISPLAY_HTML,choices=SIDE_TYPE,verbose_name="类型")
    status = models.IntegerField(default=STATUS_NORMAL,choices=STATUS_ITEM,verbose_name="状态")
    content = models.TextField(verbose_name="内容",blank=True,help_text="如果设置的不是html，可为空")
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="创建日期")
    owner = models.ForeignKey(User,verbose_name="作者",on_delete=models.CASCADE)
    class Meta:
        verbose_name = verbose_name_plural = "侧边栏"

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    @property
    def content_html(self):
        from blog.models import Post
        from comment.models import Comment

        result =''
        if self.type == self.DISPLAY_HTML:
            result = self.content
        if self.type == self.DISPLAY_LATEST:
            context = {
                'post' : Post.latest_posts()
            }
            result = render_to_string("config/blocks/sidebar_posts.html", context)
        elif self.type == self.DISPLAY_HOT:
            context = {
                'post':Post.hot_posts()
            }
            result = render_to_string("config/blocks/sidebar_posts.html", context)
        elif self.type == self.DISPLAY_COMMENT:
            context = {
                'comments' : Comment.objects.all()
            }
            result = render_to_string("config/blocks/sidebar_comments.html", context)
        return result

class Link(models.Model):
    def __str__(self):
        return self.title
    STATUS_NORMAL = 1;
    STATUS_DELETE = 0;
    STATUS_ITEM = (
        (STATUS_NORMAL, "正常"),
        (STATUS_DELETE, "删除")
    )
    title = models.CharField(max_length=512,verbose_name="标题")
    href = models.URLField(verbose_name="连接地址")
    status = models.IntegerField(default=STATUS_NORMAL,choices=STATUS_ITEM,verbose_name="状态")
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    weight = models.IntegerField(default=1,choices=zip(range(1,6),range(1,6)),verbose_name="重量",help_text="权重高展示顺序靠前")
    owner = models.ForeignKey(User,verbose_name="作者",on_delete=models.CASCADE)
    class Meta:
        verbose_name=verbose_name_plural = "链接"

