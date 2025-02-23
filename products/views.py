from django.shortcuts import render
from .models import Products

# Create your views here.
def productsView(request):

    productos = Products.objects.first()

    return render(request, "products/index.html", {
        "productos": productos
    })