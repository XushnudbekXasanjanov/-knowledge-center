from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
         model = User
         fields = "__all__"


class DirectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directions
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = "__all__"


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = "__all__"

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = "__all__"