from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente
from .serializers import ClienteSerializer
# Create your views here.


# ViewSets define the view behavior.
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    
