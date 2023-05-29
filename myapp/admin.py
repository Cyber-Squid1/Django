from django.contrib import admin

# from myapp.models import Blog,Author,Entry,Category,Product,UserRegister
from myapp.models import *
# Register your models here.

admin.site.register(Category)

class FeedbackRegister(admin.ModelAdmin):
    list_display = ('email','phonenumber','message')
admin.site.register(Feedback,FeedbackRegister)

class ProductRegister(admin.ModelAdmin):
    list_display=['productcategory','productname','price','quantity']
    list_filter=['productcategory']
admin.site.register(Products,ProductRegister)

class UserRegister(admin.ModelAdmin):
    list_display=['name','email','phone']
admin.site.register(User,UserRegister)