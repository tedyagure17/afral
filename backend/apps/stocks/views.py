from django.shortcuts import render

# Create your views here.
def manage_stocks(request):
    return render(request, "stocks/manage-stocks.html")

def stock_adjustment(request):
    return render(request, "stocks/stock-adjustment.html")

def stock_transfer(request):
    return render(request, "stocks/stock-transfer.html")
