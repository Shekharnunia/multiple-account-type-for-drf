from django.shortcuts import render, redirect

from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model #

from .forms import RegistrationForm
from .serializers import SchoolSerializer, TeacherSerializer



def register(request):
    if request.method =='POST':
        print('in')
        form = RegistrationForm(request.POST)
        print(form)
        print('in2')
        if form.is_valid():
            print('in3')
            user = form.save(commit=False)
            print('in4')
            # user.is_teacher = True
            print(user.is_teacher)
            print('in5')
            user.save()
            return redirect('/')
    else:
        print('in6')
        form = RegistrationForm()
    return render(request, 'register.html',{'form': form})


class CreateSchoolUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = SchoolSerializer


class CreateTeacherUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny 
    ]
    serializer_class = TeacherSerializer