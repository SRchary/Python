# forms.py
# ...
from django.forms import ModelForm
from .models import AuthorModel as author_m
class AuthorForm(ModelForm):
    class Meta:
        model = author_m
        fields =['author_email' ,"author_name" ,"author_phone" ,"author_address"]
