from django.urls import path

from . import views

app_name = "inventory"

urlpatterns = [
    path("products/", views.product_list, name="product-list"),
    path("products-add/", views.add_product, name="add-product"),
    path("products-stock/", views.low_stocks, name="low-stocks"),
    path("products-expired/", views.expired_products, name="expired-products"),
    path("category-list/", views.category_list, name="category-list"),
    path("sub-category-list/", views.sub_categories, name="sub-categories"),
    path("brands-list/", views.brand_list, name="brand-list"),
    path("units-list/", views.units, name="units"),
]
