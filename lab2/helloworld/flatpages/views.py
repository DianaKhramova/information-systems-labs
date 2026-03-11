#coding:utf-8
from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {})
def static_handler(request):
    return render(request, 'static_handler.html', {})
