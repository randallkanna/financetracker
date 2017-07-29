from rest_framework import generics, permissions
from .permissions import IsOwner
from .serializers import ListSerializer
from .models import List

class CreateView(generics.ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner
    )
