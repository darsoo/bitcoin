# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
    course = models.CharField('Kurs', max_length=255)
    date = models.DateTimeField('Data dodania', auto_now_add=True)

def __str__(self):
        return self.course
    
class LastTime(models.Model):
    time = models.CharField('Czas', max_length=255)
    min = models.CharField('Kurs minimalny', max_length=255)
    max = models.CharField('Kurs maxymalny', max_length=255)

def __str__(self):
        return self.course

class Current(models.Model):
    time = models.CharField('Czas', max_length=255)
    bids = models.CharField('Bids', max_length=255)
    asks = models.CharField('Ask', max_length=255)

def __str__(self):
        return self.course




# Create your models here.
