from django.shortcuts import render
from rest_framework import generics , status
from rest_framework.response import Response
from .models import blogpost
from .serializers import blogpostserializer
# Create your views here.

class blogpostlistcreate(generics.ListCreateAPIView):
    queryset = blogpost.objects.all()
    serializer_class = blogpostserializer
    def delete(self, request, *args, **kwargs):
        blogpost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class blogpostretriveupdatedestroy(generics.RetrieveDestroyAPIView):
    queryset = blogpost.objects.all()
    serializer_class = blogpostserializer
    lookup_field = "pk"
