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
class TeachersFilter(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]



    def get(self,request):
        user = request.user
        if user.types == 1:
            query = User.objects.filter(types=2)
            ser = UserSerializer(query,many=True)
            return Response(ser.data)
        else:
            return Response('xatolik')


class PaymentStudent(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        if user.types == 3:
            course = request.POST.get('course')
            summa = request.POST.get('summa')
            kod = request.POST.get('kod')
            yonalish = Directions.objects.get(course=int(course))
            # for i in User.objects.filter(types=3):
            if User.objects.filter(kod=int(kod)):
               if int(summa) >= yonalish.monthly_payment:
                             query = Payment.objects.create(is_paid=True, summa=float(summa), course_id=course,date=datetime.datetime.now())
                             ser = PaymentSerializer(query)
                             data = {
                                'Tolandi': ser.data,
                                }
                             return Response(data)

               elif int(summa) < yonalish.monthly_payment:
                         som = yonalish.monthly_payment - int(summa)
                         query = Payment.objects.create(is_paid=False, summa=float(summa), course_id=course, date=datetime.datetime.now())
                         ser = PaymentSerializer(query)

                         data = {
                             'tolandi':ser.data,
                             'toliq tolovga qancha qolganligi:' : som
                         }
                         return Response(data)

        else:
                return Response('error')




class ComplaintParents(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request):
        user = request.user
        if user.types == 5:
            types = request.POST.get('types')
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            subject = request.POST.get('subject')
            adress = request.POST.get('adress')
            query = Complaint.objects.create(types=types,name=name,phone=phone,subject=subject,adress=adress)
            ser = ComplaintSerializer(query)
            print('minasa abdulbosit aytdi')
            return Response(ser.data)



class TeachersCourses(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        user = request.user
        if user.types == 2:
            total = Course.objects.filter(teacher_id=user).count()
            query = Course.objects.filter(teacher_id=user)
            ser = CourseSerializer(query,many=True)
            data = {
                'umumiy': total,
                'kurslar': ser.data
            }
            return Response(data)

class ComplaintParents(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request):
        user = request.user
        if user.types == 5:
            message = request.POST.get('message')
            subject = request.POST.get('subject')
            complaint = Complaint.objects.create(message=message,subject=subject)
            ser = ComplaintSerializer(complaint)
            return Response(ser.data)

@api_view(["POST"])
def Register(request):
    unik = string.digits
    kod = ''.join((random.choice(unik) for i in range(4)))
    try:
        username = request.data["username"]
        password = request.data["password"]
        users = User.objects.create(username=username, password=password,kod=kod)
        token = Token.objects.create(user=users)
        login(request, users)
        return Response({"username": username, "user": users.id, "token": token.key,'kod':users.kod})
    except Exception as err:
        return Response({"error": f"{err}"})



@api_view(["POST"])
def Login(request):
    try:
        username = request.data["username"]
        password = request.data["password"]
        try:
            users = User.objects.get(username=username)
            if users is not None:
                usr = authenticate(username=username, password=password)
                if usr is not None:
                    login(request, usr)
                    token, created  = Token.objects.get_or_create(user=users)
                    data = {
                        "username": username,
                        "user_id": users.id,
                        "token": token.key
                    }
                else:
                    status = 403
                    message = "Password error"
                    data = {
                        "status": status,
                        "message": message
                    }
            else:
                status = 403
                message = "Username error"
                data = {
                    "status": status,
                    "message": message
                }
        except:
            status = 404
            message = "Bunday foydalanuvchi mavjud emas!"
            data = {
                "status": status,
                "message": message
            }
        return Response(data)
    except Exception as err:
        return Response({"error": f'{err}'})

class MonthRate(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request):
        user = request.user
        if user.types == 2:
            month = request.POST.get('month')
            student = request.POST.get('student')
            rate = request.POST.get('rate')
            if Rate.objects.filter(student_id=student,month_id=month):
                return Response('bu oyda bu oquvchiga baxo uje berilgan')
            else:
                 query = Rate.objects.create(month_id=month, student_id=student, rate=rate)
                 ser = RateSerializer(query)
                 data = {
                     "o'tdi":ser.data
                 }
                 return Response(data)

class ReplyComplaints(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request,pk):
        user = request.user
        if user.types == 1 or user.types == 4:
            s = Complaint.objects.get(id=pk)
            if s.is_replied == False:
                s.is_replied = True
                s.save()
                return Response({'ok'})
            # else:
            #     return Response('uje javob qaytarilgan')