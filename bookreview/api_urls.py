from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import AuthorViewSet, BookViewSet, ReviewViewSet

# Create a router and register our viewsets
router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'books', BookViewSet, basename='book')
router.register(r'reviews', ReviewViewSet, basename='review')

# The API URLs are determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]