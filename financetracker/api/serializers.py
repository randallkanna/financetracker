from rest_framework import serializers
from .models import List

class ListSerializer(serializers.ModelSerializer): # Serializer maps the model into json

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta: # class to map serializer to model
        model = List
        fields = ('id', 'name', 'owner', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
