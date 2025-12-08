# mahwar_social/admin.py
from django.contrib import admin
from .models import Album, Post   # لاحظ: لا يوجد SocialAccount هنا

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'size_mb', 'created_at')
    search_fields = ('name', 'user__username', 'user__email')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'created_at', 'scheduled_at')
    list_filter = ('status',)
    search_fields = ('user__username', 'content')
