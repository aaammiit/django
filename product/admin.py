from django.contrib import admin

# Register your models here.
from .models import Catagory,Product,Order_Payment,Product_order_buy

class Cat_admin(admin.ModelAdmin):
    list_display=['id','cat_img','name']

admin.site.register(Catagory,Cat_admin)


class pro_admin(admin.ModelAdmin):
    list_display=['id','catagory','pro_img','pro_name','price','desc']

admin.site.register(Product,pro_admin)



class Ord_pay_admin(admin.ModelAdmin):
    pass
admin.site.register(Order_Payment,Ord_pay_admin)



class Ord_admin(admin.ModelAdmin):
    list_display=['user','email']

admin.site.register(Product_order_buy,Ord_admin)

