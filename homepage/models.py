from __future__ import unicode_literals

from django.db import models

# Create your models here.

class News(models.Model):
	news_text = models.CharField(max_length=200)
	news_header = models.CharField(max_length=1000)
	news_date_published = models.DateTimeField('date published')

