"""
URL configuration for Web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crt/<str:p_id>',v.cart_view,name='crt'),
    path('cart_list',v.Cart_list,name='cart_list'),
    path('delete/<int:id>',v.Delete_view,name='delete'),
    path('order_list',v.Order_List_view,name='order_list'),
    path('delete_pro/<int:id>',v.Delete_pro,name='delete_pro'),
    path('about-us',v.About_view,name='about-us'),
    
   
]
