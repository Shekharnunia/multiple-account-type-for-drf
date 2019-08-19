from rest_framework import serializers
from django.contrib.auth import get_user_model # If used custom user model

UserModel = get_user_model()


class SchoolSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create(
            email=validated_data['email'],
            username=validated_data['email'],
            is_school = True
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = UserModel
        fields = ( "id", "email", "password", )


class TeacherSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create(
            email=validated_data['email'],
            username=validated_data['email'],
            is_teacher = True
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = UserModel
        fields = ( "id", "email", "password", )