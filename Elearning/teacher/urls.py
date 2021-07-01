from django.urls import path
from . import views

app_name='teacher'

urlpatterns = [
    path('',views.teacherlogin,name="teacherlogin"),
    path('teacherhome/',views.teacherhome,name="teacherhome"),
    path('Loginout/',views.Loginout,name="Loginout"),
    path('studentslist/',views.studentslist,name="studentslist"),
    path('teacher_profile/',views.teacher_profile,name="teacher_profile"),
    path('imageadd/',views.imageadd,name="imageadd"),
    path('teacher_edit/',views.teacher_edit,name="teacher_edit"),
    path('password_edit/',views.password_edit,name="password_edit"),
    path('classes/',views.classes,name="classes"),
    path('add_class/',views.add_class,name="add_class"),
    path('delete_class/<int:pk>/',views.delete_class,name="delete_class")
    
    
    
]