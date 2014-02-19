from django.db import models

# Create your models here.

def mch(length):
	return models.CharField(max_length=length)

class TimeStampedModel(models.Model):
	""" TimeStampedModel
	An abstract base class model that provides self-managed "created" and
	"modified" fields.
	"""
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	class Meta:
		get_latest_by = 'modified'
		ordering = ('-modified', '-created',)
		abstract = True



class CompanyInfo(TimeStampedModel):
	name = models.CharField(max_length=200)
	phone = mch(20)

class Address(TimeStampedModel):
	street1 = models.CharField(max_length=200)
	street2 = models.CharField(max_length=200)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=30)
	zipcode = models.CharField(max_length=15)

