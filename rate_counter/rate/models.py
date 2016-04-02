from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models


class Subject(models.Model):
    """
    Subject model representing subject from University schedule
    """
    name = models.CharField(max_length=100)
    group = models.ForeignKey('StudentGroup', related_name='subjects', null=True)


class Institute(models.Model):
    """
    Institute model representing Institute parsed from University
    """
    name = models.CharField(max_length=4)
    site_id = models.CharField(max_length=2, null=True)


class StudentGroup(models.Model):
    """
    Group representing students group in University
    """
    user = models.ForeignKey(User, related_name='student_groups', null=True)
    institute = models.ForeignKey(Institute, related_name='groups', null=True)
    name = models.CharField(max_length=15)
    site_id = models.CharField(max_length=4, null=True)

    @property
    def students_count(self):
        return self.user.all().count()


class Rate(models.Model):
    """
    Rate model representing rating of Student
    """
    user = models.ForeignKey(User, related_name='rate')
    value = models.FloatField()
