from django.contrib import admin
from django.urls import path, re_path
from accounts import views

urlpatterns = [
    path('register/', views.register),
    path('school/register/', views.CreateSchoolUserView.as_view()),
    path('teacher/register/', views.CreateTeacherUserView.as_view()),
    path('admin/', admin.site.urls),
]
