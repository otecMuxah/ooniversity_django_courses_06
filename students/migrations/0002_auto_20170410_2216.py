# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(help_text='Hold down "Control",or "Command" on a Mac, to select more then one.', to='courses.Course'),
        ),
    ]
