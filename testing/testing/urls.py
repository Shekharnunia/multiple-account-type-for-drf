from django.contrib import admin
from django.urls import path, re_path, include
from accounts import views

urlpatterns = [
    path('register/', views.register),
    re_path(r'^rest-auth/', include('rest_auth.urls')),
    path('school/register/', views.CreateSchoolUserView.as_view()),
    path('teacher/register/', views.CreateTeacherUserView.as_view()),
    path('admin/', admin.site.urls),
    re_path(r'^', include('django.contrib.auth.urls')),
    re_path(r'^silk/', include('silk.urls', namespace='silk'))
]
