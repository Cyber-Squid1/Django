from django.shortcuts import render,redirect
from django.http import HttpResponse
import razorpay
from myapp.models import *
# Create your views here.

def table(request):
    # data=User.objects.all()
    # print(data)
    # return render(request,'table.html',{"data":data})
    data=User.objects.filter(phone=7016104220)
    print(data)
    return render(request,'table.html',{"data":data})

def SignIn(request):
    if request.method=="POST":
        name1=request.POST['name']
        email1=request.POST['email']
        password1=request.POST['pswd']
        phone1=request.POST['phone']
        data=User(name=name1,email=email1,password=password1,phone=phone1)
        data.save()
        check=User.objects.filter(email=email1)
        if check:
            return render(request,'SignIn.html',{'messagesignin':"User already exists with this email"})
        else:
            return redirect('Login')
    return render(request,'SignIn.html')

def Login(request):
    if request.method=="POST":
        email1=request.POST['email']
        password1=request.POST['pswd']
        try:
            data=User.objects.get(email=email1,password=password1)
            if data:
                request.session['email']=data.email
                print("Session id:",request.session['email'])
                return redirect('Home')
            else:
                return render(request,'Login.html',{'message':'Please enter valid credentials.'})
        except :
            return render(request,'Login.html',{"message":'Please enter valid credentials.'})
    return render(request,'Login.html')

def Logout(request):
    if 'email' in request.session.keys():
        del request.session['email']
        return redirect('Home')
    else:
        return redirect('Home')

def Contactus(request):
    if request.method=="POST":
        fname1=request.POST['fname']
        lname1=request.POST['lname']
        phone=request.POST['mob']
        email1=request.POST['mail']
        message1=request.POST['feedback']
        data=Feedback.objects.create(firstname=fname1,lastname=lname1,email=email1,phonenumber=phone,message=message1)
        return render(request,'contactus.html',{"data":data})
    return render(request,'contactus.html')

def product_all(request):
    data=Products.objects.all()
    return render(request,'product_table.html',{"data":data})

def Home(request):
    if 'email' in request.session.keys():
        isLoggedIn=request.session['email']
        categorydata=Category.objects.all()
        return render(request,'Home.html',{"categorydata":categorydata,"isLoggedIn":isLoggedIn})
    else:
        categorydata=Category.objects.all()
        return render(request,'Home.html',{"categorydata":categorydata})
    

def CategoryWiseProduct(request,id):
    categoryWiseData=Products.objects.filter(productcategory=id)
    print("Category data:",categoryWiseData.values('productcategory_id'))
    return render(request,'CategoryWise.html',{"categoryWiseData":categoryWiseData})

def SingleProduct(request,id):
    SingleProductdata=Products.objects.get(pk=id)
    return render(request,'productget.html',{"SingleProductdata":SingleProductdata})

def OrderView(request):
    if 'email' in request.session:
        sessionData=request.session['email']
        orderData=Order.objects.filter(userEmail=sessionData)
        productList=[]
        for i in orderData:
            productDict={}
            productData=Products.objects.get(id=i.productid)
            productDict['name']=productData.productname
            productDict['img']=productData.productimg
            productDict['price']=productData.price
            productDict['quantity']=i.productqty
            productDict['date']=i.orderDate
            productDict['transcationid']=i.transactionId
            productList.append(productDict)
        return render(request,'orderview.html',{"sessionData":sessionData,"productList":productList})

def Profile(request):
    if request.method=='GET':
        userdata=User.objects.get(email=request.session['email'])
        return render(request,'profile.html',{"userdata":userdata})

def EditProfile(request):
    # if request.session['email']:
    #     if request.method=='POST':
    #         newname=request.POST['name']
    #         newname=request.POST['name']
    return render(request,'EditProfile.html')
   
def ChangePassword(request):
    if 'email' in request.session.keys():
        if request.method=="POST":
            oldpass1=request.POST['oldpass']
            print("Old:",oldpass1)
            dbdata=User.objects.get(email=request.session['email'])
            print("DB:",dbdata.password)
            if oldpass1 == dbdata.password:
                newpass1=request.POST['newpass']
                print("New: ",newpass1)
                User.objects.filter(email=request.session['email']).update(password=newpass1)
                print("Success")
                Logout(request)
                return redirect('Login')
            else:
                print("Failed1")
                return render(request,'ChangePass.html')
    else:
        print("Failed2")
        return render(request,'ChangePass.html')
    return render(request,'ChangePass.html')


def BuyNow(request):
    if 'email' in request.session:
        loggedinuser=User.objects.get(email=request.session['email'])
        if request.method=="POST":
            request.session['productid']=request.POST['id']
            request.session['quantity']="1"
            request.session['userid']=loggedinuser.pk
            request.session['username']=loggedinuser.name
            request.session['userEmail']=loggedinuser.email
            request.session['userContact']=loggedinuser.phone
            productdetails=Products.objects.get(id=request.POST['id'])
            request.session['orderAmount']=productdetails.price
            request.session['paymenyMethod']="Razorpay"
            request.session['transactionId']=""
            

RAZOR_KEY_ID=""
RAZOR_KEY_SECRET=""
client=razorpay.Client(auth=(RAZOR_KEY_ID,RAZOR_KEY_SECRET))

def razorpayVieww(request):
    currency='INR'
    amount=int(request.session['orderAmount'])*100
    razorpay_order=client.order.create(dict(amount=amount,currency=currency))