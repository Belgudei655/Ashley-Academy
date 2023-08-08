from django.contrib import admin
from .models import Course, Subject, Lesson,Test

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'description')
    list_filter = ('course',)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'yt_link')
    list_filter = ('subject__course', 'subject')

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('test_question','answer1','answer2','answer3','answer4','correct_answer')
    list_filter = ('lesson',)
