from django.db import models


class  LanguagesModelManager(models.Manager):
    def all(self ,*args ,**kwargs):
        qs = super(LanguagesModelManager, self).all(*args ,**kwargs).filter(active =True)
        return qs


# Create your models here.
class Languages(models.Model):
    name= models.CharField(max_length=120, verbose_name="language_name")
    code = models.CharField(max_length=120)
    active = models.BooleanField(default=True)
   # other = LanguagesModelManager()

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

class Framework(models.Model):
    name = models.CharField(max_length=120)
    framework_language = models.ForeignKey(Languages,on_delete=models.CASCADE)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.feamework_language
    def __unicode__(self):
        self.feamework_language

class  LanguagesModelManager(models.Manager):
    def all(self ,*args ,**kwargs):
        qs = super(LanguagesModelManager, self).all(*args ,**kwargs).filter(active =True)
        return qs
