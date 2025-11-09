from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    """
    ModelForm for Student model with custom styling.
    """
    class Meta:
        model = Student
        fields = ['name', 'email', 'age', 'course']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter full name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email address',
                'required': True
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter age',
                'min': '1',
                'max': '150',
                'required': True
            }),
            'course': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter course name',
                'required': True
            }),
        }
        labels = {
            'name': 'Student Name',
            'email': 'Email Address',
            'age': 'Age',
            'course': 'Course',
        }
