from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.description = 'The city that never sleeps'
    dest1.days = '7 days'
    dest1.rating = '7 star'
    return render(request, 'index.html' , {'dest1' : dest1})


