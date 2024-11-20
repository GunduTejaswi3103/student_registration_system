from django.shortcuts import render, get_object_or_404, redirect
from Student_List.models import Student,Contact_Us,JobOpening
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def mainpage(request):
    return render(request,"application1/webpage.html")

def home(request):
    return render(request,"application1/home.html")

def about_us(request):
    return render(request,"application1/about_us.html")


@csrf_exempt
def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        contact = Contact_Us(name=name, email=email, subject=subject, messages=message)
        contact.save()
        
        return redirect('/contact_us/')    
    return render(request,'application1/contact_us.html')


def careers(request):
    jobs = JobOpening.objects.all() 
    context = {
        'jobs': jobs
    }
    return render(request, 'application1/careers.html', context)


def registration(request):
    return render(request,"application1/registration.html")

def getall_students(request):
    Data=Student.objects.all()
    return render(request,'application1/student_display.html', {'students':Data})
 
@csrf_exempt
def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        roll_number = request.POST.get('roll_number')
        email = request.POST.get('email')
        course = request.POST.get('course')
        dob = request.POST.get('dob')
        father_name = request.POST.get('fathername')
        mother_name = request.POST.get('mothername')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phn_num')
        hobbies = request.POST.getlist('hobbies')
        percentage = request.POST.get('per')
        coaching = request.POST.get('coaching')
        hostel_day = request.POST.get('hostel-day')
        address = request.POST.get('address')
        about = request.POST.get('about')
        uploadphoto = request.FILES.get('photo')

        student = Student(
            name=name,
            roll_number=roll_number,
            email=email,
            course=course,
            dob=dob,
            father_name=father_name,
            mother_name=mother_name,
            gender=gender,
            phone_number=phone_number,
            hobbies=','.join(hobbies),
            percentage_marks=percentage,
            coaching=coaching,
            hostel_day=hostel_day,
            address=address,
            about_yourself=about,
            student_photo=uploadphoto,

        )
        student.save()
        return JsonResponse({'message': 'Student added successfully!'})
    return JsonResponse({'error': 'Invalid request'}, status=400)



   
def delete_student(request,pk):
    student=Student.objects.get(pk=pk)
    if request.method == 'POST':
        # pass
        student.delete()
    return redirect('/students')


@csrf_exempt
def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.roll_number = request.POST.get('roll_number')
        student.email = request.POST.get('email')
        student.course = request.POST.get('course')
        student.dob = request.POST.get('dob')
        student.father_name = request.POST.get('fathername')
        student.mother_name = request.POST.get('mothername')
        student.gender = request.POST.get('gender')
        student.phone_number = request.POST.get('phn_num')
        hobbies = request.POST.getlist('hobbies')
        student.hobbies = ','.join(hobbies)  # Save hobbies as a comma-separated string
        student.percentage_marks = request.POST.get('per')
        student.coaching = request.POST.get('coaching')
        student.hostel_day = request.POST.get('hostel-day')
        student.address = request.POST.get('address')
        student.about_yourself = request.POST.get(
            'about')
        uploadphoto = request.FILES.get('photo')
        if uploadphoto:
            student.student_photo = uploadphoto

        student.save()
        return redirect('/students')
    return render(request, 'application1/edit_student.html', {'student': student, 'is_editing': True})
