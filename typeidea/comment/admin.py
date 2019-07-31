from django.contrib import admin
from .models import Comment
from typeidea.custom_site import custom_site

# Register your models here.

@admin.register(Comment,site=custom_site)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["Target","nickname","content","website","created_time"]
    # list_filter = ["Target"]
    fields = (
        ("Target","nickname"),
        ("email","website"),
        "content",
    )
    search_fields = ["Target__title"]
    actions_on_bottom = True
    actions_on_top = True

    save_on_top = True
