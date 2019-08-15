from django.db import models
from django.urls import reverse_lazy
# Create your models here.


class Tire(models.Model):
    width = models.IntegerField()
    sidewall = models.IntegerField()
    rim = models.IntegerField()

    def get_absolute_url(self):
        return reverse_lazy('tire_list')

        # def _get_full_size(self):
        #	return '%s-%s-%s' % (str(self.width), str(self.sidewall), str(self.rim))
        #full_size =  property(_get_full_size)
