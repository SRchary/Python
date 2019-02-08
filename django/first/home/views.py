from django.shortcuts import render
from .models import Publisher

# Create your views here.
def index(request):
	p = Publisher(publisher_name ="RAVI")
	p.save()
	
	context ={}
	context['title'] ="home"
	context["data"] = Publisher.objects.all()
	return render(request , "home/index.html" ,context)
	
