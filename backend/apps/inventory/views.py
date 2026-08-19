from django.shortcuts import render

# Create your views here.
def product_list(request):
    return render(request, "inventory/product-list.html")

def add_product(request):
    return render(request, "inventory/add-product.html")

def low_stocks(request):
    return render(request, "inventory/low-stocks.html")

def expired_products(request):
    return render(request, "inventory/expired-products.html")

def category_list(request):
    return render(request, "inventory/category/category-list.html")

def sub_categories(request):
    return render(request, "inventory/category/sub-categories.html")

def brand_list(request):
    return render(request, "inventory/brands/brand-list.html")

def units(request):
    return render(request, "inventory/units/units.html")

