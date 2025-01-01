from django.shortcuts import render
from .models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html',{'products': products})


def product_list(request):
    query = request.GET.get('q')  # Get the search query from the URL
    if query:
        # Filter products based on the search query
        product_search = Product.objects.filter(name__icontains=query)
    else:
        product_search = []

    return render(request, 'product_list.html', {'product_search': product_search})
