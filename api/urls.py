from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet, CommentViewSet, PostViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

