from django.db import models

# Create your models here.

class Rates(models.Model):
  poke_num = models.IntegerField(default = 0)
  poke_name = models.CharField(max_length = 150)
  poke_rate = models.IntegerField(default = 0)