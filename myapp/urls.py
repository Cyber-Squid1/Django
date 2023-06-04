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
    path('editprofile/',EditProfile,name='EditProfile'),
    path('product_all/',product_all),
    path('product_filter/<int:id>/',CategoryWiseProduct,name="productfilter"),
    path('product_get/<int:id>/',SingleProduct,name="productget"),
    path('search/',searchProduct,name="SearchProducts"),
    path('forgotpassword/',ForgotPassword,name="Forgotpassword"),
    path('otp/',VerifyOTP,name="Otp"),
    path('changepasswordotp/',ChangePassowrdUsingOTP,name="passwordchangeotp"),
]