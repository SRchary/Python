from django.db import models

# Create your models here.

class AuthorModel(models.Model):
	author_name =models.CharField(max_length =50)
	author_phone =models.CharField(max_length =12)
	author_email =models.CharField(max_length =50)
	author_address =models.TextField(max_length =250)

	def __unicode__(self):
		return self.author_name





