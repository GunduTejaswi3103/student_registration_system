from django.contrib import admin
from Student_List.models import Student,Contact_Us,JobOpening


class Student_Admin(admin.ModelAdmin):
    list_display = ['name', 'course', 'percentage_marks', 'roll_number' ]
admin.site.register(Student,Student_Admin)


class Contact_Us_Admin(admin.ModelAdmin):
    list_display=['name','email','subject','messages']
admin.site.register(Contact_Us,Contact_Us_Admin)    

class JobOpening_Admin(admin.ModelAdmin):
    list_display=['location', 'position', 'years_of_experience', 'qualification',
        'teaching_experience', 'key_requirements', 'type', 'pay_range',
        'schedule', 'contact', 'work_location'
]
admin.site.register(JobOpening,JobOpening_Admin)  
