from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from .models import LogForm
from django.contrib.auth.models import User
from product.models import Catagory,Product
from django.views.generic import CreateView,FormView,UpdateView,DeleteView,TemplateView
from django.contrib import messages

from .models import Pr_Form,Profile

# Create your views here.


def home(request):
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
    
    return render(request,'home.html',data)

def Resister(request):
    if request.method=='POST':
        fr=UserCreationForm(request.POST)
        fr.save()
        # messages.success(request,'Your Profile Has Been Resister Sucessfully') 
        return redirect('/')
       
    else:
        form=UserCreationForm()
        context={'form':form}
        messages.warning(request,'Some thing Went Wrong Please Check!') 
        return render(request,'sineup.html',context)
    


def login_view(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pasw=request.POST.get('password')
        user=authenticate(User,username=uname,password=pasw)
        
        if user is not None:
            request.session['uid']=user.id
            login(request,user)
            messages.success(request,'You Have Login Sucessfully') 
            return redirect('/')
        else:
            lo=LogForm()
            data={'form':lo}
            messages.warning(request,'Some thing Went Wrong Please Check Username And Password!') 
            return render(request,'login.html',data)

    else:
        lo=LogForm()
        data={'form':lo}
        return render(request,'login.html',data)



def logout_view(request):
    logout(request)
    messages.success(request,'You Have Logout Sucessfully') 
    return redirect('/')


def profile_view(request):
    upid=request.session.get('uid')
    user=User.objects.get(id=upid)
    if request.method=='POST':
        img=request.POST.get('profile_pic')
        f_n=request.POST.get('first_name')
        l_n=request.POST.get('Last_name')
        em=request.POST.get('email')
        dob=request.POST.get('dob')
        add=request.POST.get('address')

        pf=Profile()
        pf.profile_pic=img
        pf.first_name=f_n
        pf.Last_name=l_n
        pf.email=em
        pf.dob=dob
        pf.address=add
        pf.user=user
        pf.save()
        messages.success(request,'Your Profile Created Sucessfully') 
        return redirect('/')
        
    else:
        fr=Pr_Form()
        fe={'form':fr}
        return render(request,'profile.html',fe)
    

def Profile_show(request):
    upid=request.session.get('uid')
    user=User.objects.get(id=upid)
    list_pro=Profile.objects.filter(user=upid)
    data={'list':list_pro}
    return render(request,'tt.html',data)


class update(UpdateView):
    model=Profile
    fields=['first_name','Last_name','email','address']
    template_name='update.html'
    success_url='/'

    


    

