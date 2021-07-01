from django.urls import path
from . import views




urlpatterns = [
    path('',views.adminlogin,name="adminlogin"),
    path('adminhome/',views.adminhome,name="adminhome"),
    path('signout/',views.signout,name="signout"),
    path('standard/',views.standard,name="standard"),
    path('add_standard/',views.add_standard,name="add_standard"),
    path('class_delete/<int:pk>/',views.class_delete,name="class_delete"),
    path('student_data/',views.student_data,name="student_data"),
    path('studentdelete/<int:pk>/',views.studentdelete,name="studentdelete"),
    path('blockstudent/<int:pk>/',views.blockstudent,name="blockstudent"),
    path('Teacher/',views.Teacher,name="Teacher"),
    path('addteacher/',views.addteacher,name="addteacher"),
    path('blockteacher/<int:pk>/',views.blockteacher,name="blockteacher"),
    path('teacherdelete/<int:pk>/',views.teacherdelete,name="teacherdelete"),
    path('sample_video/<int:pk>/',views.sample_video,name="sample_video"),
    path('ordered_data/',views.ordered_data,name="ordered_data")

]