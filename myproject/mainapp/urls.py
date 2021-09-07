from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from myproject.api import router
from .views import *
from knox import views as knox_views

urlpatterns = [
    path('', views.project, name='project'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('cart/', views.cart, name='cart'),
    path('check/', views.check, name='check'),
    path('contact/', views.contact, name='contact'),
    path('loginregistration/', views.loginregistration, name='loginregistration'),
    path('myaccount/', views.loginregistration, name='myaccount'),
    path('orderdetails/', views.orderdetails, name='orderdetails'),
    path('orderhistory/', views.orderhistory, name='orderhistory'),
    path('productdetails2/', views.productdetails2, name='productdetails2'),
    path('singleblog/', views.singleblog, name='singleblog'),
    path('wishlist/', views.wishlist, name='wishlist'),


    path('login/', LoginAPI.as_view(), name='login'),
    path('api/', include(router.urls), name='app'),

    path('api/login/logout/', knox_views.LogoutView.as_view(), name='logout'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)