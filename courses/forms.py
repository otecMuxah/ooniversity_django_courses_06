#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from courses.models import Lesson, Course


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = []


class LessonModelForm(forms.ModelForm):
    class Meta:
        model = Lesson
        exclude = []
