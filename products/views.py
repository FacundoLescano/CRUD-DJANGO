from django.shortcuts import render
from .models import Products
from django.views.generic import ListView

# Create your views here.

class PublisherListView(ListView):
    model = Products
    context_object_name = "productos"