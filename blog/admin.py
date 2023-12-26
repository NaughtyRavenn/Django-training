from django.contrib import admin
from .models import post, comment


class commentInline(admin.TabularInline):
    model = comment


class postAdmin(admin.ModelAdmin):
    ordering = ["id"]
    list_display = ["id", "title", "date"]
    list_filter = ["date"]
    search_fields = ["title"]
    inlines = [commentInline]


admin.site.register(post, postAdmin)
