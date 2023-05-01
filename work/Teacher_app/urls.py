from django.urls import path
from . import views

app_name = 'Teacher_ap'


urlpatterns = [
    path('teacher-dashbord/', views.Teacher_Dashbord, name='teacher_dashbord'),
    path('teacher-view-books/', views.Teacher_View_Books, name='teacher_view_book'),
]
