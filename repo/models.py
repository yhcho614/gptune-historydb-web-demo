from django.db import models
import jsonfield

# Create your models here.

class PerfFile(models.Model):
    app_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    perf_data = jsonfield.JSONField()
    pub_date = models.DateTimeField('date published')
