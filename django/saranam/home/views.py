from django.shortcuts import render

# Create your views here.
from .models import Languages ,Framework
def index(request):
    languages = Languages.objects.all()
    context_data ={"languages":languages}
    return render(request , "home/index.html" ,context_data )
