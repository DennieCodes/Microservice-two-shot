from django.db import models


# Create your models here.
# set locationVO
# class LocationVO(models.Model):
#     # get the href as a charfield with max_length=200
#     import_href = models.CharField(max_length=200, unique=True)
#     name = models.CharField(max_length=200)


class Hats(models.Model):
    name = models.CharField(max_length=200, default="default_value")
 


    def __str__(self):
        return self.name
