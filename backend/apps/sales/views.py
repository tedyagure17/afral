from django.shortcuts import render

# Create your views here.
def invoice(request):
    return render(request, "sales/invoice.html")

def online_orders(request):
    return render(request, "sales/online-orders.html")

def pos_orders(request):
    return render(request, "sales/pos-orders.html")

def quotation_list(request):
    return render(request, "sales/quotation-list.html")

def sales_return(request):
    return render(request, "sales/sales-returns.html")