from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Course, Subject, Lesson, Test
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
import json

def navigation(request):
    return render(request, "navigationBar.html")

def courses(request):
    return render(request, "navigationCourses.html")

def dashboard(request):
    return render(request, "dashboard.html")

def disCourses(request, tag_text):
    button_number = 1
    subject = Subject.objects.get(name=tag_text)
    lessons = Lesson.objects.filter(subject=subject)

    lesson_names = [lesson.title for lesson in lessons]
    lesson_ytlinks = [lesson.yt_link for lesson in lessons]
    
    if not lesson_names or not lesson_ytlinks:
        return render(request, "noLesson.html")
    else:
        if request.method == 'GET':
            button_text = request.GET.get('button_text')
            if button_text:
                button_number = int(button_text)
            specificListValue = lesson_names[button_number - 1]
            ytSpecificLink = lesson_ytlinks[button_number - 1]
        
        return render(request, "subjectCourse.html", {
            'courseTitle':tag_text,
            'SubList':lesson_names,
            'unitNumber':button_number,
            'subTitle':specificListValue,
            'yt_link':ytSpecificLink,
        })

def JSON_Courses(request):
    courses = Course.objects.all()
    data = []

    for course in courses:
        subjects = course.subject_set.all()
        subjects_data = []

        for subject in subjects:
            lessons = subject.lesson_set.all()
            lessons_data = []

            for lesson in lessons:

                tests = lesson.test_set.all()
                tests_data = []
                for test in tests:
                    tests_data.append({
                        'test_question': test.test_question,
                        'answer1': test.answer1,
                        'answer2': test.answer2,
                        'answer3': test.answer3,
                        'answer4': test.answer4,
                        'correct_answer':test.correct_answer,
                    })

                lessons_data.append({
                    'title': lesson.title,
                    'yt_link': lesson.yt_link,
                    'tests': tests_data,
                })

                

            subjects_data.append({
                'name': subject.name,
                'description': subject.description,
                'lessons': lessons_data,
            })

        data.append({
            'name': course.name,
            'description': course.description,
            'subjects': subjects_data,
        })
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

def renderTest(request):
    
    return render(request, "test.html")