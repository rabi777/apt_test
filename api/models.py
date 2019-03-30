from django.db import models


# Create your models here.


class Counter(models.Model):
    data_request = models.IntegerField(default=1)

    def __int__(self):
        return int(self.data_request)
