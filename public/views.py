from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main_public(request):
    return HttpResponse("Public site")
