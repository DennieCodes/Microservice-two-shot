from django.db import models


class Hats(models.Model):
    fabric = models.CharField(max_length=200)
    style = models.CharField(max_length=200)#!this is style_name
    color = models.CharField(max_length=200)

