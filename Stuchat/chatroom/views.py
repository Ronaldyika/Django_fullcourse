from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import RegisterStudent,RegisterTeacher,Assigment
from .forms import teacherregistrationform,studentregistrationform
from django.contrib.auth import login,authenticate

# Create your views here.
def index(request):
    return render(request,'index.html')

def TeacherLogin(request):
    queryset = RegisterTeacher.objects.all()
    if request.method == 'POST':
            teacheremail = request.POST['teacheremail']
            teacherpassword = request.POST['teacherpassword']

            user = authenticate(request , teacheremail = teacheremail,
                                teacherpassword = teacherpassword)
            
            if user is not None:
                login(request,user)
                return redirect('teachersite')
            else:
                return render(request,'teacher/registration/teacherlogin.html',{'invalid':'invalid credentials '})
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
    form = teacherregistrationform()
    if request.method == 'POST':
        teachername = request.POST['teachername']
        teacheremail = request.POST['teacheremail']
        teacherimage = request.POST['teacherimage']
        teacherpassword = request.POST['teacherpassword']

        new_user = RegisterTeacher.objects.create(teachername = teachername,teacheremail = teacheremail,
                                    teacherimage = teacherimage,teacherpassword = teacherpassword)
        

        new_user.save()
        user = authenticate(teachername = teachername,teacheremail = teacheremail,
                                    teacherimage = teacherimage,teacherpassword = teacherpassword)
        login(request,user)
        return redirect('teacherlogin')
    
    return render(request,'teacher/registration/teacherregistration.html',{'form':form})
def teachersite(request):
    queryset = RegisterTeacher.objects.all()
    context = {"queryset":queryset}
    return render(request,'teacher/chat/teachersite.html',context)

def studentsite(request):

    return render(request,'student/chat/studentsite.html')