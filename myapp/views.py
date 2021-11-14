from django.shortcuts import render
from . models import Student



def student_list(request):
    students=Student.objects.all()
    
    return render(request , 'myapp/studentlist.html' , {'students':students})



def student_details( request , pk) :
    student=Student.objects.get(id = pk)
    return render(request , 'myapp/studentdetails.html' , {'student':student})
    
