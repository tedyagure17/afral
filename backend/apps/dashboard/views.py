from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "dashboard/index.html")

def admin_dashboard(request):
    return render(request, "dashboard/admin-dashboard.html")

def sales_dashboard(request):
    return render(request, "dashboard/sales-dashboard.html")