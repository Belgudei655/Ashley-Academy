from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Course, Subject, Lesson, Test
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
import json

mathList = ['Algebra','Geometry','Trigonometry','Number Theory','Adding','Subtracting','Division','Factoring','Non Number']
physicList = ['Classical Physics','Quantum Physics','Electro Magnetism','Thermodynamics']
chemList =['Organic Chemistry', 'Inorganic Chemistry', 'Experimental Chemistry']
testPrepList =['GAT','SAT','IELTS','JLPT']
artList =['Modern Art','Fancy Art','Old Art','Unique Art']
languageList =['Japanese','English','German','Spanish']
lifeSkillsList =['How to buy house','How to buy car','How to buy bank','How to change citizenship']
economicsList =['Macro Economics', 'Micro Economics', 'How money works', 'Y do u need money']
biologyList =['Cell','Gene','Telomere','DNA']

trigSubList = ['Unit circle', 'Trigonometric equation', 'Trigonometric inequalities']

def navigation(request):
    return render(request, "navigationBar.html")

def courses(request):
    return render(request, "navigationCourses.html", {
        'mathList': mathList,
        'physicList': physicList,
        'chemList':chemList,
        'testPrepList':testPrepList,
        'artList':artList,
        'languageList':languageList,
        'lifeSkillsList':lifeSkillsList,
        'economicsList':economicsList,
        'biologyList':biologyList,
    })

def dashboard(request):
    return render(request, "dashboard.html")

def disCourses(request, tag_text):
    button_number = 1
    if request.method == 'GET':
        button_text = request.GET.get('button_text')
        if button_text:
            button_number = int(button_text)
        specificListValue = trigSubList[button_number - 1]
    return render(request, "subjectCourse.html", {
        'courseTitle':tag_text,
        'trigSubList':trigSubList,
        'unitNumber':button_number,
        'subTitle':specificListValue
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