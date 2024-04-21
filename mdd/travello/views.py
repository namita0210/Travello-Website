from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):

    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.description = 'The city that never sleeps'
    dest1.days = '7 days'
    dest1.rating = '5 star'
    dest1.img='1.png'

    dest2 = Destination()
    dest2.name = 'Hyderabad'
    dest2.description = 'Biryani First'
    dest2.days = '4 days'
    dest2.rating = '3 star'

    dest3 = Destination()
    dest3.name = 'Bangalore'
    dest3.description = 'Silicon Valley of India'
    dest3.days = '4 days'
    dest3.rating = '7 star'

    dests = [dest1,dest2,dest3]

    return render(request, 'index.html' , {'dests' : dests})


