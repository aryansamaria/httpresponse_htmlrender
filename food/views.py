from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def veg(request):
    return HttpResponse('<h1>Hey Vegitarians</h1>')

def nonveg(request):
    return render(request,'nonveg.html')

