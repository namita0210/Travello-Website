from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html',{'name' : 'Namita'})

def add(request):
    val1 = int(request.POST["num1"])
    val2 = int(request.POST["num2"])
    res = val1+val2
    return render(request , 'result.html' , {'result' : res})

def bmi(request):
    feet = int(request.POST["f1"])
    inches = int(request.POST["i1"])
    weight = int(request.POST["w"])
    intoInch = (feet*12) + inches
    output = (weight * 703)/ intoInch**2
    return render(request, 'result.html', {'result' : output})    
