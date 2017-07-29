from rest_framework import serializers
from .models import List

class ListSerializer(serializers.ModelSerializer): # Serializer maps the model into json
    class Meta: # class to map serializer to model
        model = List
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
