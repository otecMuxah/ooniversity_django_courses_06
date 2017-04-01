#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from math import sqrt
from quadratic.forms import QuadraticForm
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def quadratic_results(request):
    context = {}

    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            context['a'] = a = form.clean_a()
            context['b'] = b = form.cleaned_data['b']
            context['c'] = c = form.cleaned_data['c']
            context['discriminant'] = my_discr = b * b - 4 * a * c
            if my_discr == 0:
                context['x1'] = x1 = -b / (2 * a)
                context[
                    'result'] = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {x1}'.format(
                    x1=str(x1))
            elif my_discr > 0:
                context['x1'] = x1 = (-b + sqrt(my_discr)) / (2 * a)
                context['x2'] = x2 = (-b - sqrt(my_discr)) / (2 * a)
                context[
                    'result'] = 'Квадратное уравнение имеет два действительных корня: x1 = {x1}, x2 = {x2}'.format(
                    x1=str(x1), x2=str(x2))
            else:
                context[
                    'result'] = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    else:
        form = QuadraticForm()
    context['form'] = form


    #
    # def validate(data):
    #     number = data
    #     if number == str():
    #         error_message = 'коэффициент не определен'
    #     else:
    #         try:
    #             number = int(data)
    #             error_message = str()
    #         except:
    #             error_message = 'коэффициент не целое число'
    #     return error_message, number
    #
    # arguments_from_url = request.GET
    # context['a'] = arguments_from_url['a'] if arguments_from_url.__contains__('a') else str()
    # context['b'] = arguments_from_url['b'] if arguments_from_url.__contains__('b') else str()
    # context['c'] = arguments_from_url['c'] if arguments_from_url.__contains__('c') else str()
    # context['error_message_a'], a = validate(context['a'])
    # context['error_message_b'], b = validate(context['b'])
    # context['error_message_c'], c = validate(context['c'])
    # if a == 0:
    #     context['error_message_a'] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
    #     context['discriminant'] = str()
    #     context['result'] = str()
    # elif a == str() or b == str() or c == str():
    #     context['discriminant'] = str()
    #     context['result'] = str()
    # else:
    #     context['discriminant'] = b * b - 4 * a * c
    #     if context['discriminant'] < 0:
    #         context['result'] = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    #     elif context['discriminant'] == 0:
    #         x1 = -b / (2 * a)
    #         context['result'] = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {x1}'.format(x1=str(x1))
    #     elif context['discriminant'] > 0:
    #         x1 = (-b + sqrt(context['discriminant'])) / (2 * a)
    #         x2 = (-b - sqrt(context['discriminant'])) / (2 * a)
    #         context['result'] = 'Квадратное уравнение имеет два действительных корня: x1 = {x1}, x2 = {x2}'.format(x1=str(x1), x2=str(x2))
    #
    #     if context['discriminant'] != str():
    #         context['discriminant'] = 'Дискриминант: {discriminant}'.format(discriminant=str(context['discriminant']))

    return render(request, 'quadratic/results.html', context)
