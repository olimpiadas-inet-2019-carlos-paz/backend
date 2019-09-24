from django.db import models

# Create your models here.


class Exposition (models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    creation_date = models.DateField()
    description = models.TextField(max_length=240)
