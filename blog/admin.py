from django.contrib import admin
from .models import post


class postAdmin(admin.ModelAdmin):
    ordering = ["id"]
    list_display = ["id", "title", "date"]
    list_filter = ["date"]
    search_fields = ["title"]


admin.site.register(post, postAdmin)
