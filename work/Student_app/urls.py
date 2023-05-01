from django.urls import path
from . import views
app_name = 'student'


urlpatterns = [
    path('student-dashbord/', views.Student_dashbord, name='student_dashbord'),
    path('student-profile/', views.Student_profile, name='student_profile')
]
