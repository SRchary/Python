from django.shortcuts import render

# Create your views here.
def index(request):
    context_data ={}
    return render(request , "home/index.html" ,context_data )
