from django.urls import path
from .views import *
from .main import *


urlpatterns = [
    path('filterteacherss/', TeachersFilter.as_view()), # filter qiladi barcha teacherlarni
    path('payment/',PaymentStudent.as_view()), # to'lov
    path('complaints/',ComplaintParents.as_view()), # ota onalar jaloba tashlaydi
    path('register/', Register), # registratsiya
    path('Login/', Login), # login
    path('view-complaints/', ViewComplaints.as_view()), # jalbalarni korish faqat direktor va menejer
    path('view-students/', ViewStudents.as_view()), # studentlarni korish
    path('create-course/', CreateCourse.as_view()), #error bor
    path('attandence/', AttandenceView.as_view()), # davomatni ko'rish
    path('teacher-courses/',TeachersCourses.as_view()), # har bir oqituvchi ozini kurslarini koradi
    path('rate/',MonthRate.as_view()), # baholash oylik
    path('create-directions/',CreateDirections.as_view()), # yonalishlar create qilish
]