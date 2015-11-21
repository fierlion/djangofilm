from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, null=True, blank=True)
    movielength = models.IntegerField(default=0)
    theater = models.ForeignKey(Theater, null=True)

class Theater(models.Model):
    name = models.CharField(max_length=200)
    chambers = models.IntegerField(default=0)

