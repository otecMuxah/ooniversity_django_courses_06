from django.shortcuts import render, redirect
from django.contrib import messages
from students.forms import StudentModelForm
from students.models import Student
from courses.models import Course
from django.views.decorators.csrf import csrf_exempt


def list_view(request):
    data = request.GET

    if data:
        course_id = data['course_id']
        course = Course.objects.get(id=course_id)
        students_list = Student.objects.filter(courses__id=course_id)

        context = {
            'students_list': students_list,
            'current_course': course,
        }
    else:
        students_list = Student.objects.all()
        context = {
            'students_list': students_list
        }

    return render(request, 'students/list.html', context)


def detail(request, student_id):
    student = Student.objects.get(id=student_id)

    context = {
        'student': student
    }

    return render(request, 'students/detail.html', context)


@csrf_exempt
def create(request):
    context = {}
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid:
            form.save()
            message = "Student '{name} {surname}' has been successfully added".format(name=form.name, surname=form.surname)
            messages.success(request, message)
            return redirect('/students/')
    else:
        form = StudentModelForm()

    context['form'] = form
    return render(request, 'students/add.html', context)


@csrf_exempt
def edit(request, student_id):
    context = {}
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Info on the student has been successfully changed.")
            return redirect('students:edit', student_id=student_id)
    else:
        form = StudentModelForm(instance=student)
    context['form'] = form

    return render(request, 'students/edit.html', context)

@csrf_exempt
def remove(request, student_id):
    context = {}
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        student.delete()
        message = "Info on {name} {surname} has been successfully deleted".format(name=student.name, surname=student.surname)
        messages.success(request, message)
        return redirect('/students/')
    form = StudentModelForm(student)
    context['student'] = student
    context['form'] = form
    return render(request, 'students/remove.html', context)