from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, "welcome.html")


def results(request):
    return render(request, "results.html")
