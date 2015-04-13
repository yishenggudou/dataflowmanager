from django.db import models
from django.contrib import admin
# Create your models here.

class DataField(models.Model):
	FIELD_TYPE = (
		('S', 'String'),
		('I', 'Int'),
		('L', 'Large'),
	)
	name = models.CharField(max_length=30)
	info = models.CharField(max_length=30)
	field_type =  models.CharField(max_length=30, choices=FIELD_TYPE)

class DataReport(models.Model):
	name = models.CharField(max_length=30)
	info = models.CharField(max_length=30)
	datafield = models.ManyToManyField(DataField)


class DataDW(models.Model):
	name = models.CharField(max_length=30)
	info = models.CharField(max_length=30)
	datafield = models.ManyToManyField(DataField)


class DataDM(models.Model):
	name = models.CharField(max_length=30)
	info = models.CharField(max_length=30)
	datafield = models.ManyToManyField(DataField)


admin.site.register(DataField)
admin.site.register(DataDM)
admin.site.register(DataReport)
admin.site.register(DataDW)