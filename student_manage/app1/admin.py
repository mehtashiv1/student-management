from django.contrib import admin
from .models import StudentModel
# Register your models here.
class EmployeeADmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'password']

admin.site.register(StudentModel, EmployeeADmin)