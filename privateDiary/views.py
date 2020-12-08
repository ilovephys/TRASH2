from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

def helloworldfunc(request):
    responseObject = HttpResponse("<h1>HelloWorld</h1>")
    return responseObject

class helloworldClass(TemplateView):
    template_name = "hello.html"
