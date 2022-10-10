from rest_framework.response import Response
from rest_framework import authentication, permissions
from .serializer import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
import random
import string
import datetime
from django.contrib.auth import login, logout, authenticate
from rest_framework.authtoken.models import Token
from .models import *


class AttandenceView(APIView):
    def post(self, request):
        qr_code = request.POST.get("qr_code")
        print(qr_code)
        user = User.objects.get(qr_code=qr_code)
        attandence = Attendance.objects.filter(user=user)
        if attandence.count() > 0:
            if attandence.last().in_out == False:
                Attendance.objects.create(user=user, in_out=True)
                return Response({"message": "in"})
            else:
                Attendance.objects.create(user=user, in_out=False)
                return Response({"message": "out"})
        else:
            Attendance.objects.create(user=user, in_out=True)
            return Response({"message": "in"})


class CreateCourse(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request):
        user = request.user
        if user.types == 4:
            student = request.POST.getlist('student')
            print(student)
            query = Course.objects.create(students_id=student,have_place=True)
            ser = CourseSerializer(query)
            return Response(ser.data)

class ViewStudents(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.types == 1 or user.types == 4:
            query = User.objects.filter(types=3)
            return Response(UserSerializer(query,many=True).data)


class ViewComplaints(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        user = request.user
        if user.types == 1:
            query = Complaint.objects.all()
            ser = ComplaintSerializer(query,many=True)
            return Response(ser.data)
        elif user.types == 4:
            query = Complaint.objects.filter(types=2)
            ser = ComplaintSerializer(query,many=True)
            return Response(ser.data)
        else:
            return Response('sizga mumkinmas')


class CreateDirections(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request):
        user = request.user
        if user.types == 4:
            name = request.POST.get('name')
            duration = request.POST.get('duration')
            monthly_payment = request.POST.get('monthly_payment')
            hour = request.POST.get('hour')
            max_pupil = request.POST.get('max_pupil')
            query = Directions.objects.create(name=name,duration=duration,monthly_payment=monthly_payment,hour=hour,max_pupil=max_pupil)
            ser = DirectionsSerializer(query)
            return Response(ser.data)

class ComplaintParents(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request):
        user = request.user
        if user.types == 5:
            message = request.POST.get('message')
            subject = request.POST.get('subject')
            comp = Complaint.objects.create(message=message,subject=subject)
            ser = ComplaintSerializer(comp)
            return Response(ser.data)
