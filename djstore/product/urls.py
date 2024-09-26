from django.urls import path, include
from . import views
from .views import LatestProductsList, ProductDetail, CategoryDetail


urlpatterns = [

    path('latest-products', LatestProductsList.as_view()),
    path('products/search/', views.search),
    path('products/<slug:category_slug>/<slug:product_slug>', ProductDetail.as_view()),
    path('products/<slug:category_slug>/', CategoryDetail.as_view()),
]
