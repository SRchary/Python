from django.db import models

# Create your models here.

class contactme(models.Model):
    name       = models.CharField( max_length = 50   )
    email      = models.EmailField(max_length = 50  )
    address1   = models.CharField(max_length  = 50  )
    address2   = models.CharField(max_length  = 50  )
    city       = models.CharField(max_length  = 50  )
    state      = models.CharField(max_length  = 50  )
    zip        = models.CharField(max_length  = 50  )
    send_email = models.BooleanField(default=False )


    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name

