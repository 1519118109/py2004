from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    print('111')
    return HttpResponse('111')

def login(request):
    print('login')
    return HttpResponse('login')