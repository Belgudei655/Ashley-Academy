from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Course, Subject, Lesson

mathList = ['Algebra','Geometry','Trigonometry','Number Theory']
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

def test(request, course_id):
    # Retrieve the Course object with the given course_id
    course = Course.objects.get(pk=course_id)

    # Retrieve all subjects associated with the course
    subjects = course.subjects.all()

    # Pass the course and subjects to the template
    return render(request, 'test.html', {'course': course, 'subjects': subjects})