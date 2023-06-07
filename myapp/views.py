import random
import razorpay
from myapp.models import *
from django.db.models import Q
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
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
        check=User.objects.filter(email=email1)
        if check:
            return render(request,'SignIn.html',{'messagesignin':"User already exists with this email"})
        else:
            data=User(name=name1,email=email1,password=password1,phone=phone1)
            data.save()
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
    if 'email' in request.session:
        if request.method=="GET":
            userData=User.objects.get(email=request.session['email'])
            return render(request,'Contactus.html',{"userData":userData,"isLoggedIn":1})
        if request.method=="POST":
            name1=request.POST['name']
            phone=request.POST['mob']
            email1=request.POST['mail']
            message1=request.POST['feedback']
            data=Feedback.objects.create(name=name1,email=email1,phonenumber=phone,message=message1)
            return render(request,'Contactus.html',{"data":data,"isLoggedIn":1,"message":"Your Query has been recorded"})
        return render(request,'Contactus.html',{"data":data,"isLoggedIn":1})
    else:
        if request.method=="POST":
            name1=request.POST['name']
            phone=request.POST['mob']
            email1=request.POST['mail']
            message1=request.POST['feedback']
            data=Feedback.objects.create(name=name1,email=email1,phonenumber=phone,message=message1)
            return render(request,'contactus.html',{"isLoggedIn":0,"message":"Your Query has been recorded"})
        return render(request,'contactus.html',{"isLoggedIn":0})

def product_all(request):
    data=Products.objects.all()
    return render(request,'product_table.html',{"data":data})

def Home(request):
    if 'email' in request.session.keys():
        # isLoggedIn=request.session['email']
        categorydata=Category.objects.all()
        return render(request,'Home.html',{"categorydata":categorydata,"isLoggedIn":1})
    else:
        categorydata=Category.objects.all()
        return render(request,'Home.html',{"categorydata":categorydata,"isLoggedIn":0})
    

def CategoryWiseProduct(request,id):
    categoryWiseData=Products.objects.filter(productcategory=id)
    return render(request,'CategoryWise.html',{"categoryWiseData":categoryWiseData})

def SingleProduct(request,id):
    SingleProductdata=Products.objects.get(productid=id)
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
        return render(request,'profile.html',{"userdata":userdata,"isLoggedIn":1})

def EditProfile(request):
    userdata=User.objects.get(email=request.session['email'])
    if request.method=='POST':
        newname=request.POST['name']
        newPhone=request.POST['phone']
        User.objects.filter(email=request.session['email']).update(name=newname,phone=newPhone)
        userdata=User.objects.get(email=request.session['email'])
        return render(request,'profile.html',{"message":"Account Details have been updated successfully","userdata":userdata,"isLoggedIn":1})
    return render(request,'EditProfile.html',{"userdata":userdata,"isLoggedIn":1})
    
   
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
                return render(request,'ChangePass.html',{"isLoggedIn":1})
    else:
        print("Failed2")
        return render(request,'ChangePass.html',{"isLoggedIn":1})
    return render(request,'ChangePass.html',{"isLoggedIn":1})

def BuyNow(request):
    if 'email' in request.session:
        loggedinuser=User.objects.get(email=request.session['email'])
        if request.method=="POST":
            request.session['productid']=request.POST['proid']
            request.session['quantity']="1"
            request.session['userid']=loggedinuser.pk
            request.session['username']=loggedinuser.name
            request.session['userEmail']=loggedinuser.email
            request.session['userContact']=loggedinuser.phone
            productdetails=Products.objects.get(productid=request.POST['proid'])
            request.session['orderAmount']=productdetails.price
            request.session['paymentMethod']="Razorpay"
            request.session['transactionId']=""
            return redirect('razorpayView') 
    else:
        return redirect('Login')

RAZOR_KEY_ID="rzp_test_9viBqTs2AhJfoy"
RAZOR_KEY_SECRET="qnxki0MujgcumrjkSzeXfyew"
razorpay_client=razorpay.Client(auth=(RAZOR_KEY_ID,RAZOR_KEY_SECRET))

def razorpayView(request):
    currency='INR'
    amount=int(request.session['orderAmount'])*100
    razorpay_order=razorpay_client.order.create(dict(amount=amount,currency=currency,payment_capture='0'))
    razorpay_order_id = razorpay_order['id']
    callback_url = 'http://127.0.0.1:8000/paymenthandler/'
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url    
    return render(request,'razorpayDemo.html',context=context)

@csrf_exempt
def paymenthandler(request):
    if request.method == "POST":
        try:
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')

            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
            result=razorpay_client.utility.verify_payment_signature(params_dict)
            
            if result is not None:
                amount = int(request.session['orderAmount'])*100
                razorpay_client.payment.capture(payment_id,amount)

                orderTable = Order()
                orderTable.productid=request.session['productid']
                orderTable.productqty=request.session['quantity']
                orderTable.userId = request.session['userid']
                orderTable.userName = request.session['username']
                orderTable.userEmail = request.session['userEmail']
                orderTable.userContact = request.session['userContact']
                orderTable.address = "jamnagar"
                orderTable.orderAmount = request.session['orderAmount']
                orderTable.paymentMethod = request.session['paymentMethod']
                orderTable.transactionId = payment_id
                productData=Products.objects.get(productid=request.session['productid'])
                productData.quantity=productData.quantity-int(request.session['quantity'])
                productData.save()
                orderTable.save()
                del request.session['productid']
                del request.session['quantity']
                del request.session['userid']
                del request.session['username']
                del request.session['userEmail']
                del request.session['userContact']
                del request.session['orderAmount']
                del request.session['paymentMethod']
                return redirect('SuccessOrder')
            else:
                return HttpResponseBadRequest()
        except:
            return HttpResponseBadRequest()
    else:
        return HttpResponseBadRequest()

def OrderSuccess(request):
    if 'email' in request.session:
        a=request.session['email']
        return render(request,'order_sucess.html',{'a':a})
    else:
        return HttpResponseBadRequest()

def searchProduct(request):
    word=request.GET.get('search')
    wordset=word.split(" ")
    for i in wordset:
        searchData=Products.objects.filter(Q(Category_categoryname_icontains=1)|Q(productname_icontains=i)|Q(price_icontains=i)).distinct()
        return render(request,'product_table.html',{"searchData":searchData})


def ForgotPassword(request):
    if request.method=="POST":
        useremail=request.POST['email']
        try:
            data=User.objects.get(email=useremail)
            if data:
                def generate():
                    otp=''
                    for _ in range(6):
                        otp+=str(random.randint(0,9))
                    return otp
                onetimepass=generate()
                print(onetimepass)
                request.session['otp']=onetimepass
                send_mail(
                "Forgot Password",
                "Dear " +str(data.name)+"\n Your OTP is :"+str(onetimepass),
                "youremail",
                [useremail],
                fail_silently=False,
                )
                request.session['otpemail']=useremail
                return render(request,'otp.html',{'message':'OTP Sent To Your Email'})
            else:
                return render(request,'Forgotpassword.html',{'message':'Email Id Not Found'})
        except:
            return render(request,'Forgotpassword.html',{'message':'Email Id Not Found'})
    return render(request,'Forgotpassword.html')


def VerifyOTP(request):
    if 'otp' in request.session:
        if request.method=="POST":
            userotp=request.POST['otp']
            print("Verify otp: ",request.session['otpemail'])
            if userotp == request.session['otp']:
                return render(request,'otpchangepassword.html',{"PasswordChanged":0})
    else:
        return render(request,'Forgotpassword.html',{'message':'OTP expired.Please generate a new OTP.'})

def ChangePassowrdUsingOTP(request):
    if 'otp' in request.session:
        if request.method=="POST":
            newPassword=request.POST['newpassword']
            print(request.session['otpemail'])
            try:
                User.objects.filter(email=request.session['otpemail']).update(password=newPassword)
                del request.session['otp']
                del request.session['otpemail']
                return render(request,'otpchangepassword.html',{"PasswordChanged":1})
            except:
                return render(request,'otpchangepassword.html',{"PasswordChanged":0})
        return render(request,'otpchangepassword.html',{"PasswordChanged":0})
    else:
        return render(request,'Forgotpassword.html',{"message":"OTP expired.Please generate a new OTP."})
    
def AddToCart(request,id):
    print(0)
    if 'email' in request.session:
        print(0.1)
        if request.method=="POST":
            print(1)
            productData=Products.objects.get(productid=int(id))
            print(2)
            userData=User.objects.get(email=request.session['email'])
            print(3)
            qty=1
            addToCartData=MyCart(userId=userData.pk,productid=productData.productid,name=productData.productname,img=productData.productimg,price=productData.price,quantity=qty,totalprice=qty*productData.price,is_bought=False)
            print(4)
            addToCartData.save()
            print(5)
            return render(request,'Cart.html',{"isLoggedIn":1})
    else:
        print(6)
        return render(request,'Login.html',{"isLoggedIn":0})
# productid
# name
# img
# price
# quantity
# totalprice
# is_bought

def ViewCart(request):
    if 'email' in request.session:
        userData=User.objects.get(email=request.session['email'])
        myCartData=MyCart.objects.filter(userId=userData.pk)
        finalTotal=0
        productList=[]
        for i in myCartData:
            finalTotal+=int(i.totalprice)
            productDict={}
            productData=Products.objects.get(productid=i.productid)
            productDict['name']=productData.productname
            productDict['img']=productData.productimg
            productDict['price']=productData.price
            productDict['quantity']=i.quantity
            productDict['total']=i.totalprice
            productList.append(productDict)
        print(productList)
        return render(request,'Cart.html',{"productList":productList,"finalTotal":finalTotal,"numItemas":len(productList),"isLoggedIn":1})
    return render(request,'Cart.html',{"isLoggedIn":1})