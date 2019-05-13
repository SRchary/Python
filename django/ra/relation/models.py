from django.db import models

# Create your models here.

class Company(models.Model):
    name    = models.CharField(max_length =20,unique=True)
    address = models.TextField(max_length = 250)

    def __str__(self):
        return self.name

class Language(models.Model):
    name =models.CharField(max_length = 20)

    def __str__(self):
        return self.name



class Employe(models.Model):
    name  = models.CharField(max_length =50)
    employe_id =models.CharField(max_length=10)
    company = models.ForeignKey(Company ,on_delete =models.CASCADE )
    languages =models.ManyToManyField(Language)

    def __str__(self):
        return self.name




