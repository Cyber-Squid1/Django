from django.urls import path
from myapp.views import *

urlpatterns = [
    path('',Home,name='Home'),
    path('signin/',SignIn,name='Signin'),
    path('login/',Login,name='Login'),
    path('logout/',Logout,name='Logout'),
    path('contactus/',Contactus,name='ContactUs'),
    path('profile/',Profile,name='Profile'),
    path('changepass/',ChangePassword,name='ChangePass'),
    path('editprofile/',AddProfileImage,name='AddProfileImage'),
    # path('editprofile/',EditProfile,name='EditProfile'),
    path('product_all/',product_all),
    path('buynow/',BuyNow,name='BuyProduct'),
    path('razorpayView/',razorpayView,name='razorpayView'),
    path('paymenthandler/',paymenthandler,name='paymenthandler'),
    path('ordersuccess/',OrderSuccess,name="SuccessOrder"),
    path('product_filter/<int:id>/',CategoryWiseProduct,name="productfilter"),
    path('product_get/<int:id>/',SingleProduct,name="productget"),
    path('addtocart/',AddToCart,name="addtocart"),
    path('search/',searchProduct,name="SearchProducts"),
    path('forgotpassword/',ForgotPassword,name="Forgotpassword"),
    path('removeItem/<int:id>/',RemoveSingleItem,name="Remove1Item"),
    path('removeAllItems/',RemoveAllItems,name="RemoveAllItems"),
    path('otp/',VerifyOTP,name="Otp"),
    path('changepasswordotp/',ChangePassowrdUsingOTP,name="passwordchangeotp"),
    path('cart/',ViewCart,name="ViewCart"),
    path('shipping/',Shipping,name="Shipping"),
    path('orderView/',OrderView,name="OrderView"),
    path('VendorSignUp/',VendorSignUp,name="VendorSignUp"),
    path('vendorLogin/',VendorLogin,name="VendorLogin"),
    path('addProduct/',VendorAddProduct,name='VendorAddProduct'),
    path('vendorDashboard/',VendorDashboard,name='VendorDashboard'),
    path('stock/',VendorViewStock,name='ViewStock'),
    path('vendorLogout/',VendorLogout,name='VendorLogout'),
    path('vendorProfile/',VendorProfile,name='VendorProfile'),
]