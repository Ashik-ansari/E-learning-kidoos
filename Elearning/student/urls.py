from django.urls import path
from . import views
from django.views.generic import TemplateView




urlpatterns = [
    
    #path ('',TemplateView.as_view(template_name="index.html")),
    path('',views.index,name="index"),
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('Logout/',views.Logout,name="Logout"),
    path('otp_request/',views.otp_request,name="otp_request"),
    path('student_profile/',views.student_profile,name="student_profile"),
    path('addimage/',views.addimage,name="addimage"),
    path('editprofile/<int:pk>/',views.editprofile,name="editprofile"),
    path('otp_validate/',views.otp_validate,name="otp_validate"),
    path('editpassword/',views.editpassword,name="editpassword"),
    path('profile_edit/',views.profile_edit,name="profile_edit"),
    path('standard_details/<int:pk>/',views.standard_details,name="standard_details"),
    path('payment/<int:pk>/',views.payment,name="payment"),
    path('subject1_tutorials/',views.subject1_tutorials,name="subject1_tutorials"),
    path('subject2_tutorials/',views.subject2_tutorials,name="subject2_tutorials"),
    path('subject3_tutorials/',views.subject3_tutorials,name="subject3_tutorials"),
    path('orderpayment/',views.orderpayment,name="orderpayment"),
    path('razorpay/',views.razorpay,name="razorpay"),
    path('razorpaysuccess/',views.razorpaysuccess,name="razorpaysuccess")
    #path('paypal/',views.paypal,name="paypal")

    
]