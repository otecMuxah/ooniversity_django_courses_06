from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=6, choices=(('M', 'Male'),
                                                      ('F', 'Female')))
    phone = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    skype = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.user.username

    def get_name(self):
        return '%s' % self.user.first_name

    def get_surname(self):
        return '%s' % self.user.last_name
