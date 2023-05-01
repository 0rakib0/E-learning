from django.shortcuts import render, redirect
from HOD_Dashbord.models import Teacher, User
from clac.models import Books
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def Teacher_Dashbord(request):
    user = request.user.user_type
    if user == 'teacher':
        teacher = Teacher.objects.all().count()
        students = User.objects.filter(user_type='student').count()
        context = {
            'teacher':teacher,
            'students':students
        }
        return render(request, 'Dashbord/hod_dashbord.html', context)
    else:
        return redirect('error')
@login_required()
def Teacher_View_Books(request):
    user = request.user.user_type
    if user == 'student':
        book = Books.objects.all()
        context = {
            'book':book
        }
        return render(request, 'Teacher_dashbord/view_book.html', context)
    return redirect('error')