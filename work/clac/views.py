from django.shortcuts import render
from django.http import HttpResponse
from HOD_Dashbord.models import *
from clac.models import Category, Course, Lesson, Video, Whats_learn, Requierment, Books
from .import views
from django.db.models import Sum
# Create your views here.


def homepage(request):
    teachers = Teacher.objects.all()
    categorys = Category.objects.all()[0:8]
    courses = Course.objects.all()[0:5]
    adviser = Adviser.objects.all()
    context = {
        'teacher':teachers,
        'adviser':adviser,
        'categorys':categorys,
        'courses':courses
    }
    return render(request,'home/index.html', context)


def Course_list(request):
    course = Course.objects.all()[0:5]
    catagory_id = request.GET.get('category')
    all_course = Course.objects.all()
    course_by_category = Course.objects.filter(category=catagory_id)
    print(catagory_id)
    category = Category.objects.all()
    context = {
        'course':course,
        'category':category,
        'all_course':all_course,
        'course_by_category':course_by_category
    }
    return render(request, 'home/course_list.html', context)


def Single_course_page(request, slug):
    time_duration = None
    course = Course.objects.get(slug=slug)
    catagory_ID = course.category.id
    releted_course = Course.objects.filter(category=catagory_ID)[:5]
    corse_id = course.id
    video = Video.objects.filter(course=corse_id)
    whats_learn = Whats_learn.objects.get(course=corse_id)
    requirment = Requierment.objects.get(course=corse_id)
    time_duration = Video.objects.filter(course__slug=slug).aggregate(sum=Sum('time_duration'))
    context = {
        'course':course,
        'whats_learn':whats_learn,
        'requirment':requirment,
        'releted_course':releted_course,
        'time_duration':time_duration
    }

    return render(request, 'home/single_course.html', context)

def Book(request):
    book_list = Books.objects.filter(is_published=True)
    context = {
        'book_list':book_list
    }
    return render(request, 'home/view_book.html', context)


def Error(request):
    return render(request, 'home/error.html')