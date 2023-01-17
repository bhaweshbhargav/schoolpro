from django.db import models


# Create your models here.
class School(models.Model):
    school_name = models.CharField(max_length=500)
    university_name = models.CharField(max_length=200)
