from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from courses.models import Course, Lesson

def detail(request, course_id):
    course = Course.objects.get(id=course_id)
    lessons_list = Lesson.objects.filter(course=course)


    context = {
        'course': course,
        'lessons_list': lessons_list

    }
    return render(request, 'courses/detail.html', context)