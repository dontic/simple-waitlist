from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WaitlistItemViewSet

router = DefaultRouter()
router.register("waitlist-items", WaitlistItemViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
