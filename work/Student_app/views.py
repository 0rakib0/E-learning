from django.shortcuts import render, redirect
from Accounts.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def Student_dashbord(request):
    user = request.user.user_type
    if user == 'student':
        return render(request, 'Student/stu_dashbord.html')
    else:
        return redirect('error')

@login_required()
def Student_profile(request):
    user = request.user.user_type
    if user == 'student':
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            profile_pic = request.FILES.get('profile_pic')
            user = User.objects.get(id=request.user.id)
            print(user)
            if password != '' and password !=None:
                user.set_password(password)
            
            if profile_pic != None:
                user.profile_pic = profile_pic
            user.first_name = first_name
            user.last_name = last_name
                    
            user.save()
            messages.success(request, 'profile Succesfull Udated')
            return redirect('student:student_profile')
        return render(request, 'Student/profile.html')
    else:
        return redirect('error')
