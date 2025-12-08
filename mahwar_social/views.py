from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import Album, Post
from .serializers import AlbumSerializer, PostSerializer, SocialAccountSerializer
from accounts.models import SocialAccount

from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count

from django.contrib.auth.models import User

# Album ViewSet ✅ مع queryset
class AlbumViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated]
    queryset = Album.objects.all()  # ← أضف هذا السطر
    
    def get_queryset(self):
        return Album.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Post ViewSet ✅ مع queryset  
class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['content']          # للبحث الحر في المحتوى
    ordering_fields = ['created_at']     # السماح بالترتيب بهذا الحقل
    ordering = ['-created_at']           # افتراضيًا: الأحدث أولاً

    def get_queryset(self):
        qs = Post.objects.filter(user=self.request.user)

        status_param = self.request.query_params.get('status')
        if status_param:
            qs = qs.filter(status=status_param)

        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# SocialAccount ViewSet ✅ مع queryset
class SocialAccountViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SocialAccountSerializer
    permission_classes = [IsAuthenticated]
    queryset = SocialAccount.objects.all()  # ← أضف هذا السطر
    
    def get_queryset(self):
        return SocialAccount.objects.filter(user=self.request.user)

class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        # إحصائيات الحالات
        status_counts = (
            Post.objects
            .filter(user=user)
            .values('status')
            .annotate(count=Count('id'))
        )
        stats = {item['status']: item['count'] for item in status_counts}

        # آخر 5 منشورات
        recent_posts = (
            Post.objects
            .filter(user=user)
            .order_by('-created_at')[:5]
        )
        recent_posts_data = PostSerializer(recent_posts, many=True).data

        # حسابات السوشال
        social_accounts = SocialAccount.objects.filter(user=user, is_active=True)
        social_accounts_data = SocialAccountSerializer(social_accounts, many=True).data

        return Response({
            'stats': {
                'draft': stats.get('draft', 0),
                'scheduled': stats.get('scheduled', 0),
                'published': stats.get('published', 0),
            },
            'recent_posts': recent_posts_data,
            'social_accounts': social_accounts_data,
        })
