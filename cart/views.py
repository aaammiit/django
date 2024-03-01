from django.shortcuts import render,redirect
from product.models import Product,Catagory
from .models import Ecart
from django.contrib.auth.models import User
import datetime
from product.models import Product_order_buy
from django.contrib import messages

# Create your views here.

def cart_view(request,p_id):
    product=Product.objects.get(id=p_id)
   
    c=Ecart()
    c.product=product    
    upid=request.session.get('uid')
    user=User.objects.get(id=upid)
    c.user=user
    c.save()
    messages.success(request,'Your Product Added in Cart Sucessfully') 
   
    return redirect('/product')


def Cart_list(request):
    upid=request.session.get('uid')
    user=User.objects.get(id=upid)
    ecart=Ecart.objects.filter(user=upid)
    data={'list':ecart}
    return render(request,'cart_list.html',data)

    
# Delete Product on Cart View
def Delete_view(request,id):
    ecart=Ecart.objects.get(id=id)
    ecart.delete()
    messages.error(request,'Your Product removed From Cart Sucessfully') 
    
    return redirect('/cart_list')



def Order_List_view(request):
    upid=request.session.get('uid')
    user=User.objects.get(id=upid)
    list_pro=Product_order_buy.objects.filter(user=upid)
    data={'list':list_pro}
    return render(request,'order_list.html',data)

def Delete_pro(request,id):
    ec=Product_order_buy.objects.get(id=id)
    ec.delete()
    messages.error(request,'Your Order cancled Sucessfully') 
    
    return redirect('/order_list')




def About_view(request):
    return render(request,'about.html')


