from django.urls import path
from . import views


urlpatterns = [
    path("", views.navigation, name="navigation"),
    path("courses", views.courses, name="courses"),
    path("dashboard", views.dashboard, name="dashboard"),
    path('disCourses/<str:tag_text>/', views.disCourses, name="disCourses"),
    path('test', views.renderTest, name="test"),
    path('get_json_courses/', views.JSON_Courses, name='get_json_courses'),
    path("login", views.login, name="login"),
    path("register", views.register, name="register")
]