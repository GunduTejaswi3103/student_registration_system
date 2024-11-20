"""
URL configuration for Student_Registration_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Student_List import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.mainpage,),
    path('home',views.home,name="h_page"),
    path('about',views.about_us,name='a_page'),
    path('contact_us/',views.contact_us,name='c_page'),
    path('careers/',views.careers,name='ca_page'),
    path('registration',views.registration,name='r_page'),
    path('students/',views.getall_students,name='students'),
    path('add_student/', views.add_student, name='add_student'),
    path('student_delete/<int:pk>',views.delete_student,name='deletestudent'),
    path('student_edit/<int:pk>',views.edit_student,name='editstudent'),
]
