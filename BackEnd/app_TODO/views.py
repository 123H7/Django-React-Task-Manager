from django.shortcuts import render

from rest_framework import viewsets
from .serializers import TodoSerializers
from .models import Todo

# from django.views.generic import TemplateView
# from django.views.decorators.cache import never_cache

# index = never_cache(TemplateView.as_view(template_name="index.html"))


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializers
    queryset = Todo.objects.all()
