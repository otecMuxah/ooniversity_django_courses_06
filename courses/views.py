from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from . models import Course, Lesson

def detail(request, course_id):
    course_ = Course.objects.get(id=course_id)
    lessons_list = Lesson.objects.filter(course=course_)

    context = {
        'course': course_[0],
        'lessons_list': lessons_list
    }
    return render(request, 'detail.html', context)