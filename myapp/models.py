from datetime import date

from django.db import models


class Category(models.Model):
    categoryname = models.CharField(max_length=200)
    img = models.ImageField(upload_to='category')

    def __str__(self):
        return self.categoryname


class Products(models.Model):
    productid=models.BigAutoField(primary_key=True)
    productcategory=models.ForeignKey(Category, on_delete=models.CASCADE)
    productname=models.CharField(max_length=200)
    productimg=models.ImageField(upload_to='products')
    price=models.IntegerField(default=0)
    productdescription=models.TextField()
    quantity=models.IntegerField(default=0)
    def __str__(self):
        return self.productname
    
class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    phone=models.IntegerField()
    

class Feedback(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField()
    phonenumber=models.IntegerField()
    message=models.CharField(max_length=1000)
    
    def __str__(self):
        return self.email
    
class Order(models.Model):
    productid=models.CharField(max_length=200)
    productqty=models.CharField(max_length=200)
    userId=models.CharField(max_length=200)
    userName=models.CharField(max_length=200)
    userEmail=models.CharField(max_length=200)
    userContact=models.IntegerField()
    address=models.CharField(max_length=300)
    orderAmount=models.IntegerField()
    paymentMethod=models.CharField(max_length=200)
    transactionId=models.CharField(max_length=200)
    orderDate=models.DateTimeField(auto_created=True,auto_now=True)
    
    def __str__(self):
        return self.userName