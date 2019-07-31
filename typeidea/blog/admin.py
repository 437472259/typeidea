#-*-coding:utf-8 -*-，
from django.contrib.admin.models import LogEntry
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Post,Category,Tag
from .adminforms import PostAdminForm
from typeidea.base_admin import BaseOwnerAdmin
from typeidea.custom_site import custom_site
# Register your models here.

class PostInline(admin.TabularInline):
    fields = ("title" ,"description")
    extra = 1
    model = Post


@admin.register(Category,site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    inlines = [PostInline,]
    list_display = ('name','status','is_nav','created_time',"post__count")
    fields = ('name','status','is_nav')
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin,self).save_model(request,obj,form,change)
    def post__count(self,obj):
        return obj.post_set.count()
    post__count.short_description = "文章数量"

@admin.register(Tag,site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ("name","status","created_time")
    fields = ("name","status")

class CategoryOwnerFilter(admin.SimpleListFilter):
    title = ""
    parameter_name = "owner__category"
    #找到登陆用户下的所有人的名字和他们的id，也就是list_fields的展示项
    def lookups(self, request, model_admin):
        print(Category.objects.filter(owner=request.user).values_list("id","name"))
        return Category.objects.filter(owner=request.user).values_list("id","name")

    #self.value在点击过程中从looksup 中返回的queryset的相对应的parameter_name的值，。
    # 当选中某一个id时返回该用户的相关信息
    #点击全部时id为none，则返回全部信息
    def queryset(self, request, queryset):
        category__id=self.value()
        print(category__id)
        if category__id:
            print(1)
            return queryset.filter(category__id=self.value())
        print(2)
        return queryset

@admin.register(Post,site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    list_display = ("title","category","status","created_time","operator")
    list_display_links =["title"]
    list_filter = [CategoryOwnerFilter]
    search_fields = ["title","category__name",]
    actions_on_top = True
    actions_on_bottom = True


    save_on_top = True
    fieldsets = (
        (
            '基础配置',{
                'description' : '基础配置描述',
                'fields' : (
                    ('title','category'),
                    'status',
                )
            }
        ),
        (
            '内容',{
                'fields':(
                    'description',
                    'content',
                )
            }
        ),
        (
            '额外信息',{
                'classes' : ('collapse',),
                "fields" : ('tags',),
            }
        )
    )
    filter_horizontal = ('tags',)
    # def category__name(self,obj):
    #     return u'%s' % obj.category.name
    #     category__name.short_description = '去外键名称'
    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
        operator.short_description = '操作'

@admin.register(LogEntry,site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr','object_id','action_flag','user','change_message']