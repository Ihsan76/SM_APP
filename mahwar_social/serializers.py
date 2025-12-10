# mahwar_social/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import SocialAccount
from .models import Album, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class SocialAccountSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = SocialAccount
        fields = [
            'id',
            'user',
            'platform',
            'account_name',
            'account_id',
            'account_url',   # جديد
            'is_active',
        ]

class AlbumSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Album
        fields = ['id', 'user', 'name', 'size_mb', 'created_at']  # لا يوجد posts_count هنا



class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'content',
            'platforms',
            'status',
            'scheduled_at',
            'created_at',
        ]
        read_only_fields = ['id', 'user', 'created_at']
