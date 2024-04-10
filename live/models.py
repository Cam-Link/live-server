from django.db import models

# Create your models here.
class Live(models.Model):
  number = models.IntegerField(default=0)
  code = models.CharField(max_length=100)