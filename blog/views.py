from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog(request):
    return HttpResponse("<h2>Hello, Blog!</h2>")
