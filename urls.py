from django.urls import path
from store import views

urlpatterns = [
    
    path('search/', views.search, name='search'),
   
    # URL for Cart and Checkout
    path('add-to-cart/<slug:slug>/', views.add_to_cart_with_options, name='add_to_cart_with_options'),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('view-cart/', views.view_cart, name='view-cart'),
    
    #URL for Products
    path('product/<slug:slug>/', views.detail, name='product_related_detail'),

]
