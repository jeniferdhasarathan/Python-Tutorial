from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, AdminViewSet, ProjectViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'admins', AdminViewSet, basename='admin')
router.register(r'projects', ProjectViewSet, basename='project')

urlpatterns = [
    path('', include(router.urls)),
]
