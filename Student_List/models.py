from django.db import models

class Student(models.Model):
     
    COURSE_CHOICES = [
        ('Bi.P.C', 'Bi.P.C'),
        ('M.P.C', 'M.P.C'),
        ('M.E.C', 'M.E.C'),
        ('C.E.C', 'C.E.C'),
    ]
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    COACHING_CHOICES = [
        ('AP CET', 'AP CET'),
        ('IIT', 'IIT'),
        ('AIEEE', 'AIEEE'),
    ]
    HOSTEL_DAY_CHOICES = [
        ('Day Scholer', 'Day Scholer'),
        ('Hostel', 'Hostel'),
    ]

    name=models.CharField(max_length=100)
    roll_number=models.CharField(max_length=10)
    email=models.EmailField(blank=True, default=None, null=True)
    course=models.CharField(max_length=10,choices=COURSE_CHOICES)
    dob=models.DateField(blank=True, default=None, null=True)
    father_name=models.CharField(max_length=20, blank=True, default=None, null=True)
    mother_name=models.CharField(max_length=20, blank=True, default=None, null=True)
    gender=models.CharField(choices=GENDER_CHOICES, max_length=10)
    phone_number=models.CharField(max_length=10, blank=True, default=None, null=True)
    hobbies=models.CharField(blank=True, default=None, null=True, max_length=20)
    percentage_marks=models.DecimalField(max_digits=4,decimal_places=2)
    coaching=models.CharField(choices=COACHING_CHOICES, max_length=10)
    hostel_day=models.CharField(choices=HOSTEL_DAY_CHOICES, max_length=15)
    address=models.CharField(max_length=250, blank=True, default=None, null=True)
    about_yourself=models.CharField(max_length=500, blank=True, default=None, null=True)
    student_photo=models.ImageField(upload_to='images/', null=True)

  
class Contact_Us(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(blank=True, default=None, null=True)
    subject=models.CharField(max_length=30)
    messages=models.CharField(max_length=100)


class JobOpening(models.Model):
    location = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    years_of_experience = models.IntegerField()
    qualification = models.CharField(max_length=100)
    teaching_experience = models.BooleanField()
    key_requirements = models.TextField()
    type = models.CharField(max_length=50)
    pay_range = models.CharField(max_length=50)
    schedule = models.CharField(max_length=50)
    note = models.TextField()
    contact = models.CharField(max_length=20)
    work_location = models.CharField(max_length=100)
    


