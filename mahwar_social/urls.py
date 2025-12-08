from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlbumViewSet, PostViewSet, SocialAccountViewSet, DashboardView

router = DefaultRouter()
router.register(r'albums', AlbumViewSet, basename='album')
router.register(r'posts', PostViewSet, basename='post')
router.register(r'social-accounts', SocialAccountViewSet, basename='socialaccount')

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('', include(router.urls)),
]
