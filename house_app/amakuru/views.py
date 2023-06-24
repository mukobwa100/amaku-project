from django.shortcuts import render
from  django.http import HttpResponse

# Create your views here.
def amakuru(request):
    return render(request,'amakuru.html')
def imikino(request):
    return render(request,'imikino.html')

