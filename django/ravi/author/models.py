from django.db import models
from django.core.exceptions import ValidationError
from django.utils import  timezone


def Validate_email(email):
	if "@ravi.edu" not in email:
		raise ValidationError("This Is not Valid Email Address! This Email is not Contain @ravi.edu ")
	return email


# Create your models here.

class AuthorModel(models.Model):
	author_name     = models.CharField(max_length =50 ,verbose_name ="Author Name" )
	author_phone    = models.CharField(max_length =12)
	author_email    = models.EmailField(max_length =50 ,unique=True ,validators=[Validate_email])
	author_address  = models.TextField(max_length =250)
	created_on      = models.DateField(auto_now_add =False ,default =timezone.now)
	updated_on      = models.DateField( auto_now =True ,auto_now_add =False  )





	def __unicode__(self):
		return self.author_name

	def __str__(self):
		return self.author_name





