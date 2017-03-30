from __future__ import unicode_literals

from django.db import models
from courses.models import Course

# Create your models here.
class Student(models.Model):

    def __str__(self):
        return '{} {}'.format(self.surname, self.name)

    def full_name(self):
        return '{} {}'.format(self.surname, self.name)

    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    skype = models.CharField(max_length=200)
    courses = models.ManyToManyField(Course)
