# takes the models and convert them into json compatible data
from rest_framework import serializers
from .models import blogpost

class blogpostserializer(serializers.ModelSerializer):
    class Meta:
        model = blogpost
        fields = ["id", "title", "content", "date"]
