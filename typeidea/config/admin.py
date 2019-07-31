from django.contrib import admin
from .models import Sidebar,Link
from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin
# Register your models here.


@admin.register(Sidebar,site=custom_site)
class SidebarAdmin(BaseOwnerAdmin):
    list_display = ("title","type","content","created_time")
    list_display_links = ["type",]
    # list_filter = ("title","type")
    search_fields = ("title",)
    fields = ("title","type","content")

@admin.register(Link,site=custom_site)
class LinkAdmin(admin.ModelAdmin):
    list_display = ("title","href","status","weight","created_time","owner")
    list_display_links = ["owner",]
    # list_filter = ("owner",)
    search_fields = ("title",)
    fields = ("title","href","status","weight")


