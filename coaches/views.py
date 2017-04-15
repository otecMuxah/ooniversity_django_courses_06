from django.shortcuts import render

from coaches.models import Coach
from courses.models import Course


def detail(request, coach_id):
    coach = Coach.objects.get(id=coach_id)
    coach_courses = Course.objects.filter(coach__id=coach_id)
    assistant_courses = Course.objects.filter(assistant__id=coach_id)

    context = {
        'coach': coach,
        'coach_courses': coach_courses,
        'assistant_courses': assistant_courses,
    }

    return render(request, 'coaches/detail.html', context)