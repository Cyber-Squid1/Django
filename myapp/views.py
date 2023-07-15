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
    data=User.objects.filter(phone=7016104220)
    return render(request,'table.html',{"data":data})

def SignIn(request):
    if request.method=="POST":
        fn=request.POST['fname']
        ln=request.POST['lname']
        name1=str(fn)+" "+str(ln)
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
    if 'email' in request.session:
        SingleProductdata=Products.objects.get(productid=id)
        return render(request,'productget.html',{"SingleProductdata":SingleProductdata,"isLoggedIn":1})
    else:
        return redirect('Login')

def OrderView(request):
    if 'email' in request.session:
        sessionData=request.session['email']
        orderData=Order.objects.filter(userEmail=sessionData)
        productList=[]
        for i in orderData:
            cartData=MyCart.objects.filter(orderId=i.pk)
            for j in cartData:
                productDict={}
                productData=Products.objects.get(productid=j.productid)
                productDict['name']=productData.productname
                productDict['img']=productData.productimg
                productDict['price']=j.totalprice
                productDict['quantity']=j.quantity
                productDict['date']=i.orderDate
                productDict['transcationid']=i.transactionId
                productList.append(productDict)
        return render(request,'orderview.html',{"isLoggedIn":1,"productList":productList})
    else:
        return HttpResponseBadRequest()

def Profile(request):
    if 'email' in request.session:
        if request.method=='POST':
            fn=request.POST['firstname']
            ln=request.POST['lastname']
            name1=str(fn)+" "+str(ln)
            newPhone=request.POST['mob']
            add1=request.POST['address']
            User.objects.filter(email=request.session['email']).update(name=name1,phone=newPhone,address=add1)
            return redirect('Profile')
        userdata=User.objects.get(email=request.session['email'])
        nameList=str(userdata.name).split(" ")
        return render(request,'profile.html',{"userdata":userdata,"isLoggedIn":1,"fname":nameList[0],"lname":nameList[1]})

def AddProfileImage(request):
    return redirect('Profile')
# def EditProfile(request):
#     userdata=User.objects.get(email=request.session['email'])
#     if request.method=='POST':
#         newname=request.POST['name']
#         newPhone=request.POST['phone']
#         User.objects.filter(email=request.session['email']).update(name=newname,phone=newPhone)
#         userdata=User.objects.get(email=request.session['email'])
#         return render(request,'profile.html',{"message":"Account Details have been updated successfully","userdata":userdata,"isLoggedIn":1})
#     return render(request,'EditProfile.html',{"userdata":userdata,"isLoggedIn":1})

def ChangePassword(request):
    if 'email' in request.session.keys():
        if request.method=="POST":
            oldpass1=request.POST['oldpass']
            dbdata=User.objects.get(email=request.session['email'])
            if oldpass1 == dbdata.password:
                newpass1=request.POST['newpass']
                User.objects.filter(email=request.session['email']).update(password=newpass1)
                Logout(request)
                return redirect('Login')
            else:
                return render(request,'ChangePass.html',{"isLoggedIn":1})
    else:
        return render(request,'ChangePass.html',{"isLoggedIn":1})
    return render(request,'ChangePass.html',{"isLoggedIn":1})

def BuyNow(request):
    if 'email' in request.session:
        loggedinuser=User.objects.get(email=request.session['email'])
        if request.method=="POST":
            request.session['productid']=request.POST['proid']
            request.session['quantity']="1"
            request.session['userId']=loggedinuser.pk
            request.session['username']=loggedinuser.name
            request.session['userEmail']=loggedinuser.email
            request.session['userContact']=loggedinuser.phone
            request.session['address']=loggedinuser.address
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
            print(1)
            payment_id = request.POST.get('razorpay_payment_id', '')
            print(2)
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            print(3)
            signature = request.POST.get('razorpay_signature', '')
            print(4)

            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
            print(5)
            result=razorpay_client.utility.verify_payment_signature(params_dict)
            
            if result is not None:
                print(6)
                amount = int(request.session['orderAmount'])*100
                print(7)
                razorpay_client.payment.capture(payment_id,amount)
                print(8)

                orderTable = Order()
                # print(9)
                # orderTable.productid=request.session['productid']
                # print(10)
                # orderTable.productqty=request.session['quantity']
                print(11)
                orderTable.userId = request.session['userId']
                print(12)
                orderTable.userName = request.session['username']
                print(13)
                orderTable.userEmail = request.session['userEmail']
                print(14)
                orderTable.userContact = request.session['userContact']
                print(15)
                orderTable.address = request.session['address']
                print(16)
                orderTable.orderAmount = request.session['orderAmount']
                print(17)
                orderTable.paymentMethod = request.session['paymentMethod']
                print(18)
                orderTable.transactionId = payment_id
                # print(19)
                # productData=Products.objects.get(productid=request.session['productid'])
                # print(20)
                # productData.quantity=productData.quantity-int(request.session['quantity'])
                # print(21)
                # productData.save()
                print(22)
                orderTable.save()
                newOrderData=Order.objects.latest('id')
                print("Primary key is: ",newOrderData.pk)
                print(23)
                myCartdata=MyCart.objects.filter(userId=request.session['userId'])
                print(24)
                for i in myCartdata:
                    print("loop1")
                    i.orderId=str(newOrderData.pk)
                    print("loop2")
                    productData=Products.objects.get(productid=i.productid)
                    print("loop3")
                    productData.quantity=productData.quantity-int(i.quantity)
                    print("loop4")
                    productData.save()
                    print("loop5")
                    i.save()
                    print("loop6")
                print("loop end")
                # del request.session['productid']
                # del request.session['quantity']
                del request.session['userId']
                del request.session['username']
                del request.session['userEmail']
                del request.session['userContact']
                del request.session['address']
                del request.session['orderAmount']
                del request.session['paymentMethod']
                print(24)
                return redirect('SuccessOrder')
            else:
                print(25)
                return HttpResponseBadRequest()
        except:
            print(26)
            return HttpResponseBadRequest()
    else:
        print(27)
        return HttpResponseBadRequest()

def OrderSuccess(request):
    if 'email' in request.session:
        return render(request,'order_sucess.html',{"isLoggedIn":1})
    else:
        return HttpResponseBadRequest()

def searchProduct(request):
    word=request.GET.get('search')
    wordset=word.split(" ")
    for i in wordset:
        searchData=Products.objects.filter(Q(productname__icontains=i)|Q(price__icontains=i)).distinct() # Q(productcategory__categoryname__icontains=i)|
        return render(request,'product_table.html',{"data":searchData,"s":word})


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
    if 'email' in request.session:
        if request.method=="POST":
            qty=request.POST['quantity']
            print("Oty: ",qty)
            productData=Products.objects.get(productid=int(id))
            try:
                myCartData=MyCart.objects.get(productid=int(id))
                newQuantity=int(myCartData.quantity)+int(qty)
                newPrice=productData.price*newQuantity
                MyCart.objects.filter(productid=int(id)).update(quantity=newQuantity,totalprice=newPrice)
                return redirect('ViewCart')
            except:
                userData=User.objects.get(email=request.session['email'])
                addToCartData=MyCart(userId=userData.pk,productid=productData.productid,quantity=qty,totalprice=int(qty)*int(productData.price),orderId="0")
                addToCartData.save()
                return redirect('ViewCart')
    else:
        return render(request,'Login.html',{"isLoggedIn":0})


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
            productDict['productid']=productData.productid
            productDict['name']=productData.productname
            productDict['img']=productData.productimg
            productDict['price']=productData.price
            productDict['quantity']=i.quantity
            productDict['total']=i.totalprice
            productList.append(productDict)
        return render(request,'Cart.html',{"productList":productList,"finalTotal":finalTotal,"numItems":len(productList),"isLoggedIn":1})
    return render(request,'Cart.html',{"isLoggedIn":0})


def RemoveSingleItem(request,id):
    if 'email' in request.session:
        removeItemData=MyCart.objects.get(productid=id)
        removeItemData.delete()
        return redirect('ViewCart')
    else:
        return redirect('Login')

def Shipping(request):
    if 'email' in request.session:
        userdata=User.objects.get(email=request.session['email'])
        cartdata=MyCart.objects.filter(userId=userdata.pk,orderId="0")
        finaltotal=0
        for i in cartdata:
            finaltotal+=int(i.totalprice)
        if request.POST:
            request.session['productid']="0"
            request.session['quantity']="0"
            request.session['userId']=userdata.pk
            request.session['username']=request.POST['name']
            request.session['userEmail']=request.POST['email']
            request.session['userContact']=request.POST['phone']
            request.session['address']=request.POST['address']
            request.session['orderAmount']=request.POST['orderAmount']
            request.session['paymentMethod']="Razorpay"
            request.session['transactionId']=""
            return redirect('razorpayView')
        return render(request,'Shipping.html',{'finalorder':finaltotal,'user':userdata})
    else:
        return redirect('login1')

def RemoveAllItems(request):
    if 'email' in request.session:
        userData=User.objects.get(email=request.session['email'])
        data=MyCart.objects.filter(userId=userData.pk ,orderId="0")
        data.delete()
        return redirect('ViewCart')
    else:
        return redirect('Login')

def VendorLogin(request):
    if request.method=="POST":
        email1=request.POST['email']
        password1=request.POST['pswd']
        try:
            data=VendorRegister.objects.get(email=email1,password=password1)
            if data:
                request.session['vendorEmail']=data.email
                print("Session id:",request.session['vendorEmail'])
                return redirect('VendorDashboard')
            else:
                return render(request,'vendorogin.html',{'message':'Please enter valid credentials.'})
        except :
            return render(request,'vendorogin.html',{"message":'Please enter valid credentials.'})
    return render(request,'vendorlogin.html')

def VendorSignUp(request):
    if request.method=="POST":
        fn=request.POST['fname']
        ln=request.POST['lname']
        name1=str(fn)+" "+str(ln)
        email1=request.POST['email']
        password1=request.POST['pswd']
        phone1=request.POST['phone']
        check=VendorRegister.objects.filter(email=email1)
        if check:
            return render(request,'VendorSignUp.html',{'messagesignin':"User already exists with this email"})
        else:
            data=VendorRegister(name=name1,email=email1,password=password1,phone=phone1)
            data.save()
            return redirect('VendorLogin')
    return render(request,'vendorsignup.html')

def VendorAddProduct(request):
    if 'vendorEmail' in request.session:
        vendorData=VendorRegister.objects.get(email=request.session['vendorEmail'])
        temp=Products.objects.filter(vendorid=vendorData.pk)
        productCategoryList=[]
        for i in temp:
            categoryDict={}
            categoryDict['categoryId']=i.productcategory.pk
            categoryDict['categoryName']=i.productcategory.categoryname
            if categoryDict in productCategoryList:
                continue
            else:
                productCategoryList.append(categoryDict)
        return render(request,'vendoraddproduct.html',{"vendorLoggedIn":1,"productCategoryList":productCategoryList})
    else:
        return redirect('VendorLogin')

def VendorViewStock(request):
    return render(request,'VendorViewStock.html')

def VendorDashboard(request):
    if 'vendorEmail' in request.session:
        return render(request,'vendordashboard.html',{"vendorLoggedIn":1})
    else:
        return redirect('VendorLogin')

def VendorLogout(request):
    if 'vendorEmail' in request.session.keys():
        del request.session['vendorEmail']
        return redirect('VendorLogin')
    else:
        return redirect('VendorLogin')

def VendorProfile(request):
    return render(request,"vendorProfile.html")