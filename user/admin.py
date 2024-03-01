from django.contrib import admin

# Register your models here.
from .models import Profile

class prof_admin(admin.ModelAdmin):
   list_display=['first_name','email','dob']

admin.site.register(Profile,prof_admin)