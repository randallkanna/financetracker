from django.shortcuts import render
from rest_framework import generics
from .serializers import ListSerializer
from .models import List

class CreateView(generics.ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer

