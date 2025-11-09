from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Student
from .forms import StudentForm


def student_list(request):
    """
    View to display list of all students (READ operation).
    """
    students = Student.objects.all()
    context = {
        'students': students,
        'total_students': students.count()
    }
    return render(request, 'students/student_list.html', context)


def student_create(request):
    """
    View to create a new student (CREATE operation).
    """
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, f'Student "{student.name}" has been added successfully!')
            return redirect('student_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentForm()
    
    context = {
        'form': form,
        'title': 'Add New Student',
        'button_text': 'Add Student'
    }
    return render(request, 'students/student_form.html', context)


def student_update(request, pk):
    """
    View to update an existing student (UPDATE operation).
    """
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, f'Student "{student.name}" has been updated successfully!')
            return redirect('student_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentForm(instance=student)
    
    context = {
        'form': form,
        'title': f'Edit Student: {student.name}',
        'button_text': 'Update Student',
        'student': student
    }
    return render(request, 'students/student_form.html', context)


def student_delete(request, pk):
    """
    View to delete a student (DELETE operation).
    """
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        student_name = student.name
        student.delete()
        messages.success(request, f'Student "{student_name}" has been deleted successfully!')
        return redirect('student_list')
    
    context = {
        'student': student
    }
    return render(request, 'students/student_confirm_delete.html', context)
