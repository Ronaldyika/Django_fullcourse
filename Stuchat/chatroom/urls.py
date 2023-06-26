from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index,name='indexpage'),
    path('registerstudent/',views.Registerstudent,name='registerstudent'),
    path('registerteacher/',views.registerteacher,name='registerteacher'),
    path('studentlogin/',views.StudentLogin,name='studentlogin'),
    path('teacherlogin/',views.TeacherLogin,name='teacherlogin'),
    path('studentsite/',views.studentsite,name='studentsite'),
    path('teachersite/',views.teachersite,name='teachersite'),
]

if settings.DEBUG:

    urlpatterns +=  static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)