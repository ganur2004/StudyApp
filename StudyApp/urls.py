from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Study.views import ProductViewSet, LessonViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'lessons', LessonViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
