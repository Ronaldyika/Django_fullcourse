from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import RegisterStudent,RegisterTeacher,Assigment
from .forms import teacherregistrationform,studentregistrationform
from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request,'index.html')

def TeacherLogin(request):
    if request.method == 'POST':
        form = teacherregistrationform(request.POST)
        if form.is_valid():
            newuser = form.save()
            login(request,newuser)

            return redirect('teachersite')
    return render(request,'teacher/registration/teacherlogin.html')

def StudentLogin(request):
    image = RegisterStudent.objects.all()

    context = {
        'image':image
    }
    return render(request,'student/register/studentlogin.html',context)

def Registerstudent(request):
    if request.method == 'POST':
        studentname = request.POST['studentname']
        studentimage = request.POST['studentimage']
        username = request.POST['username']
        matricule = request.POST['matricule']
        studentpassword = request.POST['studentpassword']

        newstudent = RegisterStudent(studentname=studentname,studentimage=studentimage,
                                    username = username, matricule=matricule,studentpassword = studentpassword)
        
        newstudent.save()
        return redirect('studentlogin')

    return render(request,'student/register/studentregistration.html')

def registerteacher(request):
        if request.method == 'POST':
            form = teacherregistrationform(request.POST)
            if form.is_valid():
                newteacher = form.save() 
            # Log the user in
                login(newteacher)

                return redirect('teacherlogin')
            else:
                form = teacherregistrationform()
            return render(request, 'teacher/registration/teacherregistration.html', {'form': form})
        else:

            form = teacherregistrationform()
            return render(request, 'teacher/registration/teacherregistration.html', {'form': form})
def teachersite(request):
    queryset = RegisterTeacher.objects.all()
    context = {"queryset":queryset}
    return render(request,'teacher/chat/teachersite.html',context)

def studentsite(request):

    return render(request,'student/chat/studentsite.html')