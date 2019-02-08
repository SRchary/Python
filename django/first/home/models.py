from django.db import models

# Create your models here.
class Publisher(models.Model):
	publisher_name = models.CharField(max_length =50)
	
	def __str__(self):
		return self.publisher_name
		
	class Meta:
		ordering =( "publisher_name",)
		