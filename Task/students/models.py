from django.db import models


class Student(models.Model):
    """
    Student model for managing student records.
    """
    name = models.CharField(max_length=100, help_text="Enter student's full name")
    email = models.EmailField(unique=True, help_text="Enter student's email address")
    age = models.IntegerField(help_text="Enter student's age")
    course = models.CharField(max_length=50, help_text="Enter course name")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return f"{self.name} - {self.course}"
