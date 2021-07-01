from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from django.http import JsonResponse
from . models import Myclass
from student.models import Myclass,Students,Teachers,Order
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.core.files import File
from django.core.mail import send_mail
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files import File
import base64



# import base64
# from django.core.files.base import ContentFile
# Create your views here.

def adminlogin(request):
    if request.session.has_key('key'):
        return redirect('adminhome')
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST['password']

        if(username=='admin' and password =='12345'):
            request.session['key']='high'
            return JsonResponse('true',safe=False)
        else:
            return JsonResponse('false',safe=False)
        return redirect(admin1)         

    return render(request,"admin1/adminlogin.html")


def adminhome(request):
    return render(request,"admin1/adminhome.html")

def standard(request):
    if request.session.has_key('key'):
        myclass = Myclass.objects.all()
        return render(request,"admin1/standards.html",{'Myclass':myclass})

    else: 
        return redirect('adminlogin')

def add_standard(request):
    if request.method == 'POST':
        standards = request.POST['standard']
        price = request.POST['price']
        durations = request.POST['duration']
        sub1=request.POST['sub1']
        sub2=request.POST['sub2']
        sub3=request.POST['sub3']
        
        image1=request.POST['image1']
        format ,imgstr = image1.split(';base64,')
        ext = format.split('/')[-1]
        img1=ContentFile(base64.b64decode(imgstr),name=standards+'.'+ext)

        
        if Myclass.objects.filter(standard=standards).exists():
            messages.info(request,"This class already exist..")
            return redirect('standard')
                
        else:   
            Myclass.objects.create(standard=standards,price=price,duration=durations,image=img1,sub1=sub1,sub2=sub2,sub3=sub3)
            return JsonResponse('true',safe=False)    
    else:
        return redirect('standard')

def sample_video(request,pk):
    standard = Myclass.objects.get(id=pk)
    print(standard.standard)
    if request.method=="POST":
        video1 = request.FILES.get('video')
        standard.video=video1
        standard.save()
        return redirect('standard')

def student_data(request):
    student = Students.objects.all()
    return render(request,"admin1/student_data.html",{'students':student})

def ordered_data(request):
    order = Order.objects.all()
    return render(request,"admin1/ordered_data.html",{'orders':order})


def studentdelete(request,pk):
    student=Students.objects.get(id=pk)
    student.delete()
    return redirect('student_data')


def blockstudent(request,pk):
    student=Students.objects.get(id=pk)
    
    if  student.active == True:
        student.active =False
        student.save()
        return redirect('student_data')
    else:
        student.active=True
        student.save()
        return redirect('student_data')    


def class_delete(request,pk):
    myclass= Myclass.objects.get(id=pk)
    myclass.delete()
    return redirect('standard')

def Teacher(request):
    teacher = Teachers.objects.all()
    return render(request,"admin1/Teacher.html",{'Teachers':teacher})


def addteacher(request):
    myclass = Myclass.objects.all()
    if request.method == 'POST':

        full_name = request.POST.get('full_name1')
        username = request.POST.get('username1')
        email = request.POST.get('email1')
        mobile = request.POST.get('mobile_number1')
        qualification = request.POST.get('qualification1')
        experience = request.POST.get('experience1')
        standard = request.POST.get('standard1')
        password1 =request.POST.get('password1')
        password2 =request.POST.get('password2')

        
        if password1==password2:
            if Teachers.objects.filter(username=username).exists():
                return JsonResponse('false2',safe=False)
                   
            elif Teachers.objects.filter(email=email).exists():
                return JsonResponse('false6',safe=False)  

            elif Teachers.objects.filter(mobile_number=mobile).exists():
                return JsonResponse('false5',safe=False)     

            else:
                password = make_password(password1)
                standard1 = Myclass.objects.get(standard=standard)
                teacher = Teachers.objects.create(username=username,standard=standard1,password=password,full_name=full_name,email=email,qualification=qualification,experience=experience,mobile_number=mobile)
                teacher.save()
                print("created")
                # send_mail(
                #     'your login credential',
                #     'username is your email and password is :' +str(password2),
                #     'ashik777ask@gmail.com',
                #     ['ashik777ask@gmail.com'],
                #     fail_silently=False,
                # )
                return JsonResponse('true', safe=False)
        else:
            return JsonResponse('false4', safe=False)
        
    else:
        return render(request,"admin1/addteacher.html",{'Myclass':myclass})


def blockteacher(request,pk):
    teacher = Teachers.objects.get(id=pk)

    if  teacher.active == True:
        teacher.active =False
        teacher.save()
        return redirect('Teacher')
    else:
        teacher.active=True
        teacher.save()
        return redirect('Teacher')

def teacherdelete(request,pk):
    teacher = Teachers.objects.get(id=pk)
    teacher.delete()
    return redirect('Teacher')


def signout(request):
    request.session.flush()
    return redirect('adminlogin')    




