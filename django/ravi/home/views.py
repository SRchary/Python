from django.shortcuts import render

# Create your views here.

def index(request):
	context ={"title":"Home"}
	template = "home/index.html"
	return render(request ,template ,context)
