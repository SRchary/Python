from django.shortcuts import render ,redirect
from .models import AuthorModel as author_m
from . forms import AuthorForm as author_f


# Create your views here.

def index(request):
	context ={"title":"Authors"}
	all_authors = author_m.objects.all()
	context['all_authors'] = all_authors
	template ="author/index.html"
	return render(request ,template ,context)


def add(request):
	context ={"title":"Authors"}
	template ="author/add.html"
	return render(request ,template ,context)


def edit(request ,author_id=0):
	context ={"title":"Authors"}
	template ="author/edit.html"
	author_details  = author_m.objects.get(id=author_id)
	form = author_f(request.POST or None, instance=author_details)
	if(form.is_valid):
		'''
		author_details.author_name    = "sf" #request.POST.get('author_name')
		author_details.author_email   = "sd"#request.POST.get('author_email')
		author_details.author_phone   = "sdfsd"#request.POST.get('author_phone')
		author_details.author_address = "dfdfg dfffffff"#request.POST.get('author_address')
		author_details.save()
		print(request.POST)
		'''
		form.save()
		redirect("/author")
	
	if(  author_details  ):
		context['author_details'] = author_details
	else:
		return redirect("/author/")
	
	return render(request ,template ,context)


def view(request):
	context ={"title":"Authors"}
	template ="author/edit.html"
	return render(request ,template ,context)		