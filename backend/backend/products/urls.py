from django.urls import path

from . import views

urlpatterns = [
    # ex: /products/
    path("", views.products, name="products"),
    # ex: /products/5/
    path("<int:product_id>/", views.detail, name="detail"),
    path("<int:product_id>/similar", views.similar, name="similar")
]
