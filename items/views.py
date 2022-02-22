from django.shortcuts import render

from rest_framework import viewsets, permissions
from .serializers import ItemSerializer
from .models import Item

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('-id')
    serializer_class = ItemSerializer
