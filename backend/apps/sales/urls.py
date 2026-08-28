from django.urls import path

from . import views

app_name = "sales"

urlpatterns = [
    path("sales-invoice", views.invoice, name="invoice"),
    path("sales-online-orders", views.online_orders, name="online-orders"),
    path("sales-pos-orders", views.pos_orders, name="pos-orders"),
    path("sales-quotation-list", views.quotation_list, name="quotation-list"),
    path("sales-returns", views.sales_return, name="sales-returns"),
]
