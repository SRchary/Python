from django.db import models

# Create your models here.
class Languages(models.Model):
    name= models.CharField(max_length=120, verbose_name="language_name")
    code = models.CharField(max_length=120)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

class Framework(models.Model):
    name = models.CharField(max_length=120)
    feamework_language = models.ForeignKey(Languages,on_delete=models.CASCADE)

    def __str__(self):
        return self.feamework_language
    def __unicode__(self):
        self.feamework_language
