# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Treasure(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    material = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='treasure_images', default='/default.png')

    def __str__(self):
        return self.name

