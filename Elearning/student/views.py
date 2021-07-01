#from Elearning import student
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from . models import Myclass,Students,Order
from teacher.models import Tutorial 
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import check_password
from django.contrib import messages
import random
from twilio.rest import Client
#from django.core.cache import cache


# Create your views here.

# class index(TemplateView):
#     template_name = "index.html"

def index(request):
    myclass1=Myclass.objects.all()

    if request.user.is_authenticated: 

        #student1=Students.objects.get(user=request.user)
        try:
            student1=Students.objects.get(user=request.user)
            print(student1)
        except Students.DoesNotExist:
            student1 = None
            
       # print(student1.standard)
        if student1 is not None:
            if student1.standard != None:
                standard=Myclass.objects.get(standard=student1.standard.standard)

                context = {
                    'Myclass':myclass1,
                    'subjects':standard,
                    'students':student1
                }
                return render(request,"student/index.html",context)
            else:
                return render(request,"student/index.html",{'Myclass':myclass1,'students':student1})
        else:
            print("message")
            messages.info(request, 'username and password wrong.')
            return redirect('login')
    else:
        return render(request,"student/index.html",{'Myclass':myclass1})


@csrf_exempt
def login(request):
    # if request.session.has_key('key'):
    #     return redirect(index)

    if request.method== 'POST':
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')    

        user = User.objects.get(username=username1)

        if user.is_active == True:
            user = auth.authenticate(username=username1,password=password1)
            if user is not None:
                auth.login(request,user)
                request.session['key']='high'
                return JsonResponse('true',safe=False)
            
            else:   
                return JsonResponse('false', safe=False)

        else:
            return JsonResponse('block',safe=False)        

    else:    
        return render(request,"student/login.html")
    


def register(request):

    if request.method == 'POST':
        student_name = request.POST.get('student1')
        parent_name = request.POST.get('parent1')
        age = request.POST.get('age1')
        mobile = request.POST.get('mobile1')
        password1 = request.POST.get('pass1')
        password2 = request.POST.get('pass2')
        #standard = request.POST.get('standard1')
        email =request.POST.get('email1')
        username =request.POST.get('username1')
            
        if password1==password2:
            if User.objects.filter(username=username).exists():
                return JsonResponse('false7',safe=False) 

            if Students.objects.filter(mobile_number=mobile).exists():
                return JsonResponse('false5',safe=False)    
                   
            elif User.objects.filter(email=email).exists():
                return JsonResponse('false6',safe=False)  

            else:
                #standard1 = Myclass.objects.get(standard=standard)
                users = User.objects.create_user(password=password2,email=email,username=username)
                student = Students.objects.create(user=users,student_name=student_name,parent_name=parent_name,student_age=age,mobile_number=mobile)
                student.save()
                users.save()
                # request.session['student']=student.id
                # print(request.session['student'])
                print("created")
                
                return JsonResponse('true', safe=False)
        else:
            return JsonResponse('false4', safe=False)
    else:
        myclass = Myclass.objects.all()
        return render(request,"student/register.html",{'Myclass':myclass})


def otp_request(request):
    if request.method== 'POST':
        mobile=request.POST['mobile']
        if Students.objects.filter(mobile_number=mobile).exists():
            request.session['mobile']=mobile
            random_num=random.randint(1000,9999)
            global Otp
            Otp=random_num

            account_sid='AC5be1f48670a3e66b015732ca4d5dc8f8'
            auth_token='0f1389d0f52308a051702c59190ef726'
            client=Client(account_sid,auth_token)

            message=client.messages.create(
                body=f"your otp for login is {Otp}",
                from_='+14439988833',
                to=f'+916282117443' 
            )

            return JsonResponse('true',safe=False)
        else:
            return JsonResponse('false',safe=False)
    else:
        return render(request,"student/otp_login.html")

def otp_validate(request):
    if request.method =='POST':
        print("otp validate")
        mobile=request.session['mobile']
        users=Students.objects.get(mobile_number=mobile)
        user1 = users.user
        otp_entered = request.POST['otp1']

        global Otp

        if Otp == int(otp_entered) :
            if user1 is not None:
                auth.login(request,user1)
                request.session['key']='high'
                return JsonResponse('true',safe=False)

            else:
                return JsonResponse('false', safe=False)
        else:
            return  JsonResponse('false',safe=False)
    else:
        return render(request,"student/otp_validate.html")


def subject1_tutorials(request):
    if request.user.is_authenticated:
        users=request.user
        student=Students.objects.get(user=users)
        student1=student.standard.standard
        print(student1)
        standard1=Myclass.objects.get(standard=student1)
        sub=standard1.sub1
       
        subject1=Tutorial.objects.filter(subject=standard1.sub1,standard=standard1)
        
        print(sub)
        context = {
            'tutorials':subject1,
            'subject':student1,
            'sub':sub

        }
        return render(request,"student/classes.html",context)
    else:
        return redirect('index')

def subject2_tutorials(request):
    if request.user.is_authenticated:
        users=request.user
        student=Students.objects.get(user=users)
        student1=student.standard.standard
        print(student1)
        standard1=Myclass.objects.get(standard=student1)
        sub=standard1.sub2
        subject1=Tutorial.objects.filter(subject=standard1.sub2,standard=standard1)
        print("haooo")
        context = {
            'tutorials':subject1,
            'subject':student1,
            'sub':sub

        }
        return render(request,"student/classes.html",context)
    else:
        return redirect('index')


def subject3_tutorials(request):
    if request.user.is_authenticated:
        users=request.user
        student=Students.objects.get(user=users)
        student1=student.standard.standard
        print(student1)
        standard1=Myclass.objects.get(standard=student1)
        sub=standard1.sub3
        subject1=Tutorial.objects.filter(subject=standard1.sub3,standard=standard1)
        print("haooo")
        context = {
            'tutorials':subject1,
            'subject':student1,
            'sub':sub

        }
        return render(request,"student/classes.html",context)
    else:
        return redirect('index')



def payment(request,pk):
    
    if request.user.is_authenticated:
        myclass1=Myclass.objects.get(id=pk)
        request.session['class']=myclass1.id
        users=request.user
        student1= Students.objects.get(user=users)

        context = {
            'student':student1,
            'myclass':myclass1
        }
        return render(request,"student/payment.html",context)

    else:
        return redirect('index')

        

def orderpayment(request):
    if request.method == 'GET':           
        value=request.GET['value']
        print(value)
        if value == 'paypal':
            return JsonResponse('paypal',safe=False)
        elif value == 'razorpay':
            return JsonResponse('razorpay',safe=False)     
        else:
            return JsonResponse('false',safe=False)
    else:
        return redirect('payment')

def razorpay(request):
    if request.user.is_authenticated:
        users=request.user
        student1=Students.objects.get(user=users)
        myclass1=request.session['class']
        myclass=Myclass.objects.get(id=myclass1)
        myclass2=myclass.price
        print(myclass2)
        
        return render(request,"student/razorpay.html",{'payment':myclass2,'student':student1})

    else:
        return redirect('index')

@csrf_exempt
def razorpaysuccess(request):
    if request.method == 'POST':
        users=request.user
        student1= Students.objects.get(user=users)
        myclass1=request.session['class']
        myclass=Myclass.objects.get(id=myclass1)
        
        standard1=Myclass.objects.get(standard=myclass.standard)
        
        Order.objects.create(student=student1,standard=standard1,price=myclass.price,status="Ordered",payment_method='Razorpay')
        #this extra adding in student
        student1.standard=standard1
        student1.save()
        print(student1.standard)


        print("created")
        return redirect('index')

    else:
        return redirect('standard_details')


# def paypal(request):
#     student=request.session['student']
#     student1=Students.objects.get(id=student)
#     price=student1.standard.price

#     return render(request,"paypal.html",{'payment':price})


def student_profile(request):
    if request.user.is_authenticated:
        student1=Students.objects.get(user=request.user)
        return render(request,"student/student_profile.html",{'student':student1})

    else:
        return redirect(index)


def addimage(request):
    if request.user.is_authenticated:
        users=request.user
        image1 = request.FILES.get('imageupload')
        my=Students.objects.get(user=users)
        my.image=image1
        my.save()
        return JsonResponse('true',safe=False)

    else:
        return redirect(student_profile)        

def editprofile(request,pk):
    if request.user.is_authenticated:

        student1 =Students.objects.get(id=pk)
        myclass = Myclass.objects.all()
        return render(request,"student/edit_profile.html",{'student':student1,'Myclass':myclass})
    else:
        return redirect('index')


def profile_edit(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            
            user=request.user
            student =Students.objects.get(user=user)
            id=student.id
            pk=user.id
            
            student.student_name = request.POST.get('student1')
            student.parent_name = request.POST.get('parent1')
            student.student_age = request.POST.get('age1')
            student.mobile_number = request.POST.get('mobile1')
            #student.standard.standard = request.POST.get('standard1')
            student.user.email =request.POST.get('email1')
            student.user.username =request.POST.get('username1')
                
                

            if User.objects.filter(username=student.user.username).exclude(id=pk).exists():
                return JsonResponse('false1',safe=False)

            elif User.objects.filter(email=student.user.email).exclude(id=pk).exists():
                return JsonResponse('false2',safe=False)

            elif Students.objects.filter(mobile_number=student.mobile_number).exclude(id=id).exists():
                return JsonResponse('false3',safe=False)    


            else:
                standard1=Myclass.objects.get(standard=student.standard.standard)
                user = User.objects.filter(id=pk).update(email=student.user.email,username=student.user.username)
                student= Students.objects.filter(id=id).update(student_name=student.student_name,parent_name=student.parent_name,student_age=student.student_age,mobile_number=student.mobile_number)
                
                print("updated")
                return JsonResponse('true',safe=False)

    else:
        return redirect('index')    

def editpassword(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            current_entered=request.POST['passwords']
            current_password=request.user.password
            new_password1=request.POST['password1']
            check = check_password(current_entered,current_password)

            if check == True:
                user1 = User.objects.get(id=request.user.id)
                user1.set_password(new_password1)
                user1.save()
                return JsonResponse('true',safe=False)


        else:
            return render(request,'editprofile.html')    

    return redirect('index')

def standard_details(request,pk):
    myclass1=Myclass.objects.get(id=pk)
    return render(request,"student/standard_details.html",{'myclass':myclass1})


def Logout(request):
    request.session.flush()
    return redirect('login')    

# def select_standard(request,myclass_id):
#     print("haii")
#     myclass = Myclass.objects.get(id=myclass_id)
    
#     # return render(request,"student/register.html",{'price':myclass})




