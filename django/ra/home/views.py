from django.shortcuts import render
from . import home_forms as home_fms
from .models import contactme as contactme_m
# Create your views here.

def index(request):

    contact_form = home_fms.contact_form(request.POST or None)
    context = {"title":"Home" ,"contact_form":contact_form }
    if(contact_form.is_valid()):
        name = contact_form.cleaned_data['name']
        email = contact_form.cleaned_data['email']
        address1 = contact_form.cleaned_data['address1']
        address2 = contact_form.cleaned_data['address2']
        city = contact_form.cleaned_data['city']
        state = contact_form.cleaned_data['state']
        zip = contact_form.cleaned_data['zip']
        send_email = contact_form.cleaned_data['send_email']
        c1 = contactme_m(name=name ,email=email,address1=address1,address2=address2,city=city,zip=zip,send_email=send_email).save()
        print(c)
    else:
        print("ERROR")






    return render(request ,"home/index.html" ,context)
