from django.contrib import admin
from .models import SocialAccount


@admin.register(SocialAccount)
class SocialAccountAdmin(admin.ModelAdmin):
    list_display = ("user", "platform", "account_name", "is_active", "created_at")
    list_filter = ("platform", "is_active")
    search_fields = ("account_name", "account_id", "user__username")
