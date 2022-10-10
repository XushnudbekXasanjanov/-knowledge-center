from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['id','username', 'first_name','last_name', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Extra'), {'fields': ('types','phone', 'birth','address', 'kod', 'img', 'qr_code')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
#
admin.site.register(Complaint)
admin.site.register(Attendance)
admin.site.register(Course)
admin.site.register(Directions)
admin.site.register(Month)
admin.site.register(Rate)
# admin.site.register(RequestUserToJob)
# admin.site.register(Attendance)
admin.site.register(Lessons)
# admin.site.register(PaymentStudent)
# admin.site.register(Student)
# admin.site.register(DirectionTeachers)
# admin.site.register(CategoryDirections)
# admin.site.register(Rate)
#
