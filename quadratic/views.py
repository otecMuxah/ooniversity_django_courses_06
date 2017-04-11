# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from quadratic.forms import QuadraticForm


def quadratic_results(request):

    context={}

    if request.GET:

        form = QuadraticForm(request.GET)

        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
            # claculating discriminant
            d = b ** 2 - 4 * a * c
            if d < 0:
                result = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
            elif d == 0:
                result = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %0.1f" % (-b / 2 * a)

            else:
                x1 = (-b + d ** (1/2.0)) / (2 * a)
                x2 = (-b - d ** (1/2.0)) / (2 * a)
                result = "Квадратное уравнение имеет два действительных корня: x1 = %0.1f, x2 = %0.1f" % (x1, x2)

            context.update({ 'd' : d, 'result' : result })

    else:
        form = QuadraticForm()

    context.update({ 'form' : form })

    return render(request, "quadratic/results.html",  context )



# #! /usr/bin/env python
# # -*- coding: utf-8 -*-
#
# from django.shortcuts import render
# from math import sqrt
# from quadratic.forms import QuadraticForm
# from django.http import HttpResponse
#
#
#
# def quadratic_results(request):
#     context = {}
#
#     if request.GET:
#         form = QuadraticForm(request.GET)
#         if form.is_valid():
#             context['a'] = a = form.clean_a()
#             context['b'] = b = form.cleaned_data['b']
#             context['c'] = c = form.cleaned_data['c']
#             context['discriminant'] = discr = b * b - 4 * a * c
#             if discr == 0:
#                 context['x1'] = x1 = -b / (2 * a)
#                 context['discriminant'] = '0'
#                 context[
#                     'result'] = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {x1}'.format(
#                     x1=str(x1))
#             elif discr > 0:
#                 context['x1'] = x1 = (-b + sqrt(discr)) / (2 * a)
#                 context['x2'] = x2 = (-b - sqrt(discr)) / (2 * a)
#                 context[
#                     'result'] = 'Квадратное уравнение имеет два действительных корня: x1 = {x1}, x2 = {x2}'.format(
#                     x1=str(x1), x2=str(x2))
#             else:
#                 context[
#                     'result'] = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
#     else:
#         form = QuadraticForm()
#
#     context['form'] = form
#
#     return render(request, 'quadratic/results.html', context)
