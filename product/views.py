from django.shortcuts import render,redirect
from .models import Catagory,Product,Pro_buy_Form,Product_order_buy
from cart.models import Ecart
from .models import Order_Payment
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from Web import settings
from django.core.exceptions import MultipleObjectsReturned
import razorpay
import time
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def product_view(request):
    catagorys=Catagory.get_all_cat()
    products=Product.get_all_pro()
    catagory_id=request.GET.get('catagory')
    if catagory_id:
       products=Product.get_data_id(catagory_id)
    else:
        Product.get_all_pro()
   
    data={}
    data['dt']=products
    data['cta']=catagorys
    return render(request,'store.html',data)


def Search_view(request):
    
    srh=request.POST.get('srha')
    catagorys=Catagory.get_all_cat()   
    products=Product.objects.filter(pro_name__icontains=srh)  
    # products1=Product.objects.filter(price__icontains=srh)    
    data={}
    data['dt']=products
    # data['dt1']=products1
   
    data['cta']=catagorys
    return render(request,'store.html',data)
    


def Buy_oeder_view(request,p_id):   
    upid=request.session.get('uid')
    product=Product.objects.get(id=p_id)
    user=User.objects.get(id=upid)
    
    if request.method=='POST':       
        email=request.POST.get('email')
        address=request.POST.get('address')
        quantity=request.POST.get('quantity')
        phone=request.POST.get('contact')
        date=request.POST.get('ord_date')
        ecart=Ecart.objects.filter(user=upid)
        product=Product.objects.get(id=p_id)
        # send_mail('test', 'you','amistreetecom0101@gmail.com', [email], fail_silently=False,auth_user=None,auth_password=None)   
        c=Product_order_buy()
        c.product=product       
        c.email=email
        c.address=address
        c.quantity=quantity
        c.contact=phone
        c.ord_date=date              
        upid=request.session.get('uid')
        user=User.objects.get(id=upid)       
        c.user=user
        c.save()
        send_mail(
            "Place Order",
            "Your Order Has Been Resister Please Make Payment",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        
        messages.success(request,'Your Product Has Been Resister in Ordes page') 
        return redirect('/product')
    else:
        ord=Pro_buy_Form()
        fr={'form':ord}
        return render(request,'buy.html',fr)

def Make_payment(request,p_id):
    upid=request.session.get('uid')
    product=Product.objects.get(id=p_id)
    user=User.objects.get(id=upid)
   

    
    if request.method=='POST':
    
        
        amount=int(request.POST.get('amount'))*100
        email=request.POST.get('email')
        
        
        
        client=razorpay.Client(auth=('rzp_test_DmsiQJWNQbXlww','Cu1f0valazkgpUwdvtacMpVW'))
        payment=client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})

        pro=Order_Payment()
        pro.product=product
        pro.email=email
        pro.amount=amount
        pro.user=user
       
        

        pro.save()
        time.sleep(5)
        try:
            send_mail(
                "Payment Confirmation Pending",
                "Your Payment on the please wait for Payment conformation ",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return render(request,'pay.html',{'pay':payment})
            
        except:
            pass
        finally:
             time.sleep(20)
        send_mail(
            "Payment Done",
            "Your Payment Has Been Done ",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        
    

       

    else:
        return render(request,'pay.html')
    

    

@csrf_exempt
def Sucess(request):
    if request.method=='POST':
        
        email=request.POST.get('email')
    
        a=request.POST
        order_id=''
        for key,val in a.items():
            if key=='razorpay_order_id':
                order_id=val
                break
        user=Order_Payment.objects.filter(payment_id=order_id).first()
        
        
       
        
    
        
        
        messages.success(request,'Your Payment Has Been Recived | Your Product Has been Delliverd In your Door Around under 1-2 hour')
        return redirect('/')
    else:
        return render(request,'product')
    


