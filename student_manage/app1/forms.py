from django.forms import ModelForm
from django import forms
from .models import StudentModel
class EmployeeForm(ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}, render_value=True)
        }
