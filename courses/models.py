from django.db import models
from coaches.models import Coach

# Create your models here.
class Course(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=200)
    description = models.TextField()
    coach = models.ForeignKey(Coach,  null=True, blank=True, related_name='coach_courses')
    assistant = models.ForeignKey(Coach, null=True, blank=True, related_name='assistant_courses')

class Lesson(models.Model):

    def __str__(self):
        return self.subject

    subject = models.CharField(max_length=200)
    description = models.TextField()
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()

