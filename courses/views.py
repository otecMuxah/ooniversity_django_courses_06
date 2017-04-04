from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from courses.forms import CourseModelForm, LessonModelForm
from courses.models import Course, Lesson

def detail(request, course_id):
    course = Course.objects.get(id=course_id)
    lessons_list = Lesson.objects.filter(course=course)


    context = {
        'course': course,
        'lessons_list': lessons_list

    }
    return render(request, 'courses/detail.html', context)


@csrf_exempt
def add(request):
    context = {}
    if request.method == "POST":
        form = CourseModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            message = 'Course {} has been successfully added.'.format(data['name'])
            messages.success(request, message)
            return redirect('/')
    else:
        form = CourseModelForm()

    context['form'] = form

    return render(request, 'courses/add.html', context)


@csrf_exempt
def edit(request, course_id):
    context = {}
    course = Course.objects.get(id=course_id)

    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            message = 'The changes have been saved.'
            messages.success(request, message)
            return redirect('courses:edit', course_id=course_id)
    else:
        form = CourseModelForm(instance=course)

    context['form'] = form

    return render(request, 'courses/edit.html', context)


@csrf_exempt
def remove(request, course_id):
    context = {}
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        course.delete()
        message = 'Course {} has been deleted.'.format(course.name)
        messages.success(request, message)
        return redirect('/')
    context['course'] = course

    return render(request, 'courses/remove.html', context)

@csrf_exempt
def add_lesson(request, course_id):
    context = {}
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            message = 'Lesson {} has been successfully added.'.format(data['subject'])
            messages.success(request, message)
            return redirect('courses:detail', course_id)
    else:
        form = LessonModelForm(initial={'course': course})

    context['form'] = form

    return render(request, 'courses/add_lesson.html', context)