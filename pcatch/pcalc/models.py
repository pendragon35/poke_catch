from django.db import models

# Create your models here.

class Rates(models.Model):
  poke_num = models.IntegerField(default = 0)
  poke_name = models.CharField(max_length = 150)
  dp_rate = models.IntegerField(default = 0)
  bw_rate = models.IntegerField(default = 0)
  xy_rate = models.IntegerField(default = 0)

  def __unicode__(self):
    return "%d %s %d %d %d" % (self.poke_num, self.poke_name, self.dp_rate, self.bw_rate, self.xy_rate)