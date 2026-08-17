from django.urls import path

from . import views


app_name = "dashboard"


urlpatterns = [
    path("", views.index, name="index"),
    path("admin_dashboard/", views.admin_dashboard, name="admin-dashboard"),
    path("sales_dashboard/", views.sales_dashboard, name="sales-dashboard"),
]