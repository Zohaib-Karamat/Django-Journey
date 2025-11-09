from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'age', 'course', 'created_at']
    list_filter = ['course', 'age']
    search_fields = ['name', 'email', 'course']
    readonly_fields = ['created_at', 'updated_at']
