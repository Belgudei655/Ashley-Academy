from django.urls import path
from . import views

urlpatterns = [
    path("test/<int:course_id>/", views.test, name="test"),
    path("", views.navigation, name="navigation"),
    path("courses", views.courses, name="courses"),
    path("dashboard", views.dashboard, name="dashboard"),
    path('disCourses/<str:tag_text>/', views.disCourses, name="disCourses")
] 