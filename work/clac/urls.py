
from django. urls import path
from . import views



urlpatterns = [
   path('', views.homepage, name='index'),
   path('course-list/', views.Course_list, name='course_list'),
   path('books/', views.Book, name='books'),
   path('single-course/<slug>/', views.Single_course_page, name='single_course'),
   path('404-error/', views.Error, name='error'),
]
