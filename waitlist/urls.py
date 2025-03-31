from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WaitlistUserViewSet

router = DefaultRouter()
router.register("users", WaitlistUserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
