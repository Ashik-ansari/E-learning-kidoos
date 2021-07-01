from admin1.views import standard
from teacher.models import Tutorial
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from admin1.models import Teachers,Myclass
from student.models import Students
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.hashers import check_password




# Create your views here.


def teacherhome(request):
    
    teacher1=request.session['add']
    teacher =Teachers.objects.get(id=teacher1)

    print(teacher)
    context = {
        'teachers' :teacher
    }
    return render(request,"teacher/teacherhome.html",context)

@csrf_exempt
def teacherlogin(request):
    # if request.session.has_key('key'):
    #     #teacher1=request.session['add']
    #     #teacher =Teachers.objects.get(id=teacher1)
    #     #context = {
    #      #'teachers' :teacher
    #      #}
    #     return render(request,"teacher/teacherhome.html")

    if request.method == 'POST':
        email1 = request.POST['email']
        password1 = request.POST['password']
        print(email1)
        print(password1)

        
        #teacher= Teachers.objects.get(email=email1)

        try:
            teacher = Teachers.objects.get(email=email1)
            print(teacher)
        except Teachers.DoesNotExist:
            teacher = None
            

        if teacher is not None:                
            request.session['key']='high'
            request.session['add']=teacher.id
            
            print(request.session['add'])
            return redirect('teacher:teacherhome')

        else:
            print("message")
            messages.info(request, 'email and password wrong.')
            return redirect('teacher:teacherlogin')
                
        # else:
        #     messages.info(request, 'your are blocked.')

    else:
        return render(request,"teacher/teacherlogin.html")

        

def studentslist(request):
    teacher1=request.session['add']
    teacher = Teachers.objects.get(id=teacher1)
    print(teacher)
    teacher1 = teacher.standard
    print(teacher1)
    student1=Students.objects.filter(standard=teacher1)

    context = {
        'students':student1
    }

    return render(request,"teacher/studentslist.html",context)

def teacher_profile(request):

    teacher1=request.session['add']
    teacher2 = Teachers.objects.get(id=teacher1)
    print("jasim")
    print(teacher2)
    return render(request,"teacher/teach_profile.html",{'teacher':teacher2})

def imageadd(request):
    teacher1=request.session['add']
    image1 = request.FILES.get('imageupload')
    teacher = Teachers.objects.get(id=teacher1)
    print("teacher")
    teacher.image=image1
    teacher.save()
    return JsonResponse('true',safe=False)


def teacher_edit(request):

    if request.method == 'POST':
        print("haii")
        teacher1 = request.session['add']
        teacher = Teachers.objects.get(id=teacher1)
        print(teacher)
        id=teacher.id

        teacher.full_name = request.POST.get('full_name1')
        teacher.username = request.POST.get('username1')
        teacher.email = request.POST.get('email1')
        teacher.mobile = request.POST.get('mobile_number1')
        teacher.qualification = request.POST.get('qualification1')
        teacher.experience = request.POST.get('experience1')
       

        if Teachers.objects.filter(username=teacher.username).exclude(id=id).exists():
            return JsonResponse('false1',safe=False)

        elif Teachers.objects.filter(email=teacher.email).exclude(id=id).exists():
            return JsonResponse('false2',safe=False)

        elif Teachers.objects.filter(mobile_number=teacher.mobile_number).exclude(id=id).exists():
            return JsonResponse('false3',safe=False)    

        else:
            teacher= Teachers.objects.filter(id=id).update(full_name=teacher.full_name,username=teacher.username,email=teacher.email,mobile_number=teacher.mobile_number,qualification=teacher.qualification,experience=teacher.experience)
                
            print("updated")
            return JsonResponse('true',safe=False)


    else:
        teacher1=request.session['add']
        teacher2=Teachers.objects.get(id=teacher1)
        return render(request,"teacher/teacher_edit.html",{'teacher':teacher2}) 


def password_edit(request):
    teacher1=request.session['add']
    teacher=Teachers.objects.get(id=teacher1)

    if request.method == 'POST':
        current_entered=request.POST['passwords']
        current_password=teacher.password
        print(current_password)
        new_password1=request.POST['password1']
        check = check_password(current_entered,current_password)

        if check == True:
            print("lool")
            teacher1=Teachers.objects.get(id=teacher1)
            teacher1.password(new_password1)
            print(teacher1)
            teacher1.save()
            return JsonResponse('true',safe=False)

    else:
        return render(request,'teacher/teacher_edit.html')        

def classes(request):
    teacher1=request.session['add']
    teacher=Teachers.objects.get(id=teacher1)
    standard1=teacher.standard.standard
    print(standard1)
    standard2=Myclass.objects.get(standard=standard1)
    

    #tutorial = Tutorial.objects.filter(standard=standard2)
    subject1 = Tutorial.objects.filter(subject=standard2.sub1,standard=standard2)
    
    subject2 = Tutorial.objects.filter(subject=standard2.sub2,standard=standard2)
    
    subject3 = Tutorial.objects.filter(subject=standard2.sub3,standard=standard2)

    # tutorial = Tutorial.objects.filter(standard=standard2)

    

    context = {
        'subject':standard2,
        'subject1':subject1,
        'subject2':subject2,
        'subject3':subject3
    }
    return render(request,"teacher/tutorials.html",context)

def add_class(request):
    teacher1=request.session['add']
    teacher=Teachers.objects.get(id=teacher1)
    standard1=teacher.standard.standard

    print(standard1)

    if request.method == 'POST':
        print("post method")
        subject1=request.POST['subject']
        chapter1=request.POST['chapter']
        description1=request.POST['description']
        video1 = request.FILES.get('video')


        standard2=Myclass.objects.get(standard=standard1)
        Tutorial.objects.create(subject=subject1,chapter=chapter1,description=description1,video=video1,standard=standard2)
        print("created")
        return redirect('teacher:classes')

    else:
        return redirect('teacher:classes')

def delete_class(request,pk):
    tutorial=Tutorial.objects.get(id=pk)
    print(tutorial.description)
    tutorial.delete()
    return redirect('teacher:classes')

def Loginout(request):
    request.session.flush()
    return redirect('teacher:teacherlogin')    