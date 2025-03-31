from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from .models import WaitlistItem
from .serializers import WaitlistItemSerializer

# Create your views here.


class WaitlistItemViewSet(CreateModelMixin, GenericViewSet):
    queryset = WaitlistItem.objects.all()
    serializer_class = WaitlistItemSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
