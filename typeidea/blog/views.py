from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Category,Tag,Post
from config.models import Sidebar
from django.views.generic import DetailView,ListView
from django.db.models import Q

class CommonViewMixin:
    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'sidebars': Sidebar.get_all(),
        })
        context.update(Category.get_navs())
        return context

class IndexView(CommonViewMixin,ListView):
    queryset = Post.latest_posts()
    paginate_by = 5
    context_object_name = 'post_list'
    template_name = 'blog/list.html'

class CategoryView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data( **kwargs)
        category_id = self.kwargs.get('category_id')
        category= get_object_or_404(Category, id = category_id)
        context . update({
            'category' : category ,
        })
        return context
class TagView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data( **kwargs)
        tag_id = self.kwargs.get('tag_id')
        tag = get_object_or_404(Tag , id = tag_id)
        context.update({
            'tag':tag,
        })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        tag_id = self.kwargs.get('tag_id')
        return queryset.filter(id = tag_id)

class PostDetailView(CommonViewMixin,DetailView):
    queryset = Post.latest_posts()
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'

class SearchView(IndexView):
    def get_context_data(self,  **kwargs):
        context = super().get_context_data()
        context.update({
            'keyword' : self.request.GET.get('keyword','')
        })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.GET.get('keyword')
        if not keyword:
            return queryset
        return queryset.filter(Q(title__icontains = keyword)|Q(description__icontains=keyword))


