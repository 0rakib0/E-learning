from django.contrib import admin
from .models import Books, Category, Course, Lesson, Video, Languege, Whats_learn, Requierment, Skill_Level
# Register your models here.

admin.site.register(Books)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Video)
admin.site.register(Languege)
admin.site.register(Whats_learn)
admin.site.register(Requierment)
admin.site.register(Skill_Level)