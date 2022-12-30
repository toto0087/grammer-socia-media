from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Welcome to Grammer!</h1>")