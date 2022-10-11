from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    STATUS = (
        (1, 'director'),
        (2, 'teacher'),
        (3, 'pupil'),
        (4, 'manager'),
        (5, 'parents'),
    )
    types = models.IntegerField(choices=STATUS, default=1)
    phone = models.IntegerField(null=True, blank=True)
    birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255,null=True, blank=True)
    kod = models.IntegerField(unique=True,null=True, blank=True)
    img = models.ImageField(upload_to='students/',null=True, blank=True)
    qr_code = models.CharField(max_length=25, unique=True, null=True, blank=True)


class Directions(models.Model):
    name = models.CharField(max_length=255)
    duration = models.IntegerField()
    monthly_payment = models.IntegerField()
    hour = models.FloatField()
    max_pupil = models.IntegerField()


class Course(models.Model):
    name = models.CharField(max_length=255)
    direction = models.ForeignKey(Directions, on_delete=models.PROTECT)
    students = models.ManyToManyField(User, blank=True)
    teacher = models.ForeignKey(User, on_delete=models.PROTECT, related_name='teacher')
    have_place = models.BooleanField()
    days = models.CharField(max_length=255)


class Lessons(models.Model):
    direction = models.ForeignKey(Directions, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name



class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    in_out = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)


class Payment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    summa = models.FloatField()
    is_paid = models.BooleanField(default=False)
    date = models.DateTimeField()
    # user = models.ForeignKey(User, on_delete=models.PROTECT)


class Complaint(models.Model):
    message = models.TextField()
    subject = models.CharField(max_length=255)
    is_replied = models.BooleanField(default=False,null=True,blank=True)

class Month(models.Model):
    name = models.CharField(max_length=255)


class Rate(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE,related_name='studentlar')
    month = models.ForeignKey(Month,on_delete=models.CASCADE,related_name='oy')
    rate = models.IntegerField()


