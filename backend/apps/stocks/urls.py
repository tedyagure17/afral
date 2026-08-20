from django.urls import path

from . import views

app_name = "stocks"

urlpatterns = [
    path("stocks/", views.manage_stocks, name="manage-stocks"),
    path("stocks-adjust/", views.stock_adjustment, name="stock-adjustment"),
    path("stocks-transfer/", views.stock_transfer, name="stock-transfer"),
]
