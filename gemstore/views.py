from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

# Create your views here.
def home(request):
    title = "Home"
    return render(request, './gemstore/index.html', {'title' : title})

def index(request):
    return HttpResponse("Hello, world. You're at the gemstore index.")

def test(request):
    return HttpResponse("hello world")
