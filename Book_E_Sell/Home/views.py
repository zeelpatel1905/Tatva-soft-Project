from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    Temp = "Home.html"
    return render(request, Temp)
    # return HttpResponse("Hello, world. You're at the polls index.")