from django.contrib.auth import login
from django.shortcuts import render
from django_filters import rest_framework as filters
from knox.views import LoginView as KnoxLoginView
from rest_framework import viewsets, permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.pagination import PageNumberPagination

from .serializers import *


# Create your views here.


# Create your models here.

def project(request):
    return render(request, 'mainapp/index.html')

def about(request):
    return render(request, 'mainapp/about.html')

def blog(request):
    return render(request, 'mainapp/blog.html')

def cart(request):
    return render(request, 'mainapp/cart.html')

def check(request):
    return render(request, 'mainapp/check-out.html')

def contact(request):
    return render(request, 'mainapp/contact.html')

def loginregistration(request):
    return render(request, 'mainapp/login-registration.html')

def loginregistration(request):
    return render(request, 'mainapp/my-account.html')

def orderdetails(request):
    return render(request, 'mainapp/order-details.html')

def orderhistory(request):
    return render(request, 'mainapp/order-history.html')

def productdetails2(request):
    return render(request, 'mainapp/product-details2.html')

def singleblog(request):
    return render(request, 'mainapp/single-blog.html')

def wishlist(request):
    return render(request, 'mainapp/wishlist.html')



#api

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#login

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)

#produkt

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name','types','price')
    search_fields = ('name','types','price')

#type


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Types.objects.all()
    serializer_class = TypeSrializer

#wievs

class MessagesViewSet(viewsets.ModelViewSet):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializers