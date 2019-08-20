from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.db.models.signals import post_save
from django.dispatch import receiver



class User(AbstractUser):
    name = models.CharField(_("User's name"), blank=True, max_length=255)
    email = models.EmailField(_('Email'), max_length=255, unique=True)
    is_school = models.BooleanField('School status', default=False)
    is_teacher = models.BooleanField('teacher status', default=False)

    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=30)

    address = models.CharField(max_length=250)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pincode = models.CharField(max_length=10)
    country = models.CharField(max_length=25, default='India')

    is_school_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email



class SchoolProfile(models.Model):
    user = models.OneToOneField(User, related_name='school_profile', on_delete=models.CASCADE)

    school_address = models.CharField(max_length=250)
    school_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    school_plan_from = models.DateField(null=True)
    School_plan_to = models.DateField(null=True)

    def __str__(self):
        return self.user.email



class TeacherProfile(models.Model):
    user = models.OneToOneField(User, related_name='teacher_profile', on_delete=models.CASCADE)

    something = models.CharField(max_length=50)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_teacher:
            instance_profile = TeacherProfile(user=instance)
            instance_profile.save()
        elif instance.is_school:
            instance_profile = SchoolProfile(user=instance)
            instance_profile.save()