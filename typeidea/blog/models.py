#-*-coding:utf-8 -*-，
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    def __str__(self):
        return self.name
    STATUS_NORMAL = 1;
    STATUS_DELETE = 0;
    STATUS_ITEM = (
        (STATUS_NORMAL, "正常"),
        (STATUS_DELETE, "删除")
    )
    name = models.CharField(max_length=128,verbose_name="类别名称")
    status = models.IntegerField(default=STATUS_NORMAL,choices=STATUS_ITEM,verbose_name="状态")
    created_time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    is_nav=models.BooleanField(default=False,verbose_name="是否为导航")
    owner=models.ForeignKey(User,verbose_name="作者姓名",on_delete=models.CASCADE)
    class Meta:
        verbose_name = verbose_name_plural = '分类'

    @classmethod
    def get_navs(cls):
        categories = Category.objects.all()
        nav_categories = []
        normal_categories = []
        for cate in categories:
            if cate.is_nav:
                nav_categories.append(cate)
            else :
                normal_categories.append(cate)
        return {
            'navs' : nav_categories,
            'categories' : normal_categories
        }
class Tag(models.Model):
    def __str__(self):
        return self.name
    STATUS_NORMAL = 1;
    STATUS_DELETE = 0;
    STATUS_ITEM = (
        (STATUS_NORMAL, "正常"),
        (STATUS_DELETE, "删除")
    )
    name = models.CharField(max_length=128, verbose_name="标签名称")
    status = models.IntegerField(default=STATUS_NORMAL, choices=STATUS_ITEM, verbose_name="状态")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    owner = models.ForeignKey(User, verbose_name="作者姓名",on_delete=models.CASCADE)
    class Meta:
        verbose_name = verbose_name_plural = "标签"
class Post(models.Model):
    def __str__(self):
        return self.title
    STATUS_NORMAL = 1;
    STATUS_DELETE = 0;
    STATUS_ITEM = (
        (STATUS_NORMAL, "正常"),
        (STATUS_DELETE, "删除")
    )
    title = models.CharField(max_length=128, verbose_name="标题")
    status = models.IntegerField(default=STATUS_NORMAL, choices=STATUS_ITEM,  verbose_name="状态")
    created_time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    category=models.ForeignKey(Category,verbose_name="类别名称",on_delete=models.CASCADE)
    tags= models.ManyToManyField(Tag,verbose_name="标签名称 ")
    owner= models.ForeignKey(User,verbose_name="作者",on_delete=models.CASCADE)
    description = models.TextField(blank=True,verbose_name="描述")
    content= models.TextField(verbose_name="内容")
    pv = models.PositiveIntegerField(default= 1)
    uv = models.PositiveIntegerField(default=1)
    class Meta:
        verbose_name = verbose_name_plural = "文章"
        ordering = ['-id']


    @staticmethod
    def get_by_tag(tag_id):
        try:
            tag = Tag.objects.get(id = tag_id)
        except Tag.DoesNotExist:
            tag = None
            post_list = []
        else:
            post_list = tag.post_set.all()\
            .select_related("owner","category")
        return post_list,tag

    @staticmethod
    def get_by_category(category_id):
        try :
            category = Category.objects.get(id = category_id)
        except Category.DoesNotExist:
            category = None
            post_list = []
        else :
            post_list = category.post_set.all()\
            .select_related('owner','category')
        return post_list,category

    @classmethod
    def latest_posts(cls):
        queryset = cls.objects.all()
        return queryset

    @classmethod
    def hot_posts(cls):
        return cls.objects.filter(status = cls.STATUS_NORMAL).order_by('-pv')
