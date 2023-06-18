from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse('<h1>main page</h>')

def categories(request, catid):
    if request.POST:
        print(request.POST)
    return HttpResponse(f'<h1>this my categories</h><p>{catid}</p>')

def archive(request, year):
    if int(year)>2023:
        return redirect('home')
    return HttpResponse(f'<h1>this my archive</h><p>{year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>this page not found</h1>')
