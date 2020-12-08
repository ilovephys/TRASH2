from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import BlogModel

# Create your views here.

def helloworldfunc(request):
    responseObject = HttpResponse("HelloWorld")
    return responseObject

class BlogList(ListView):
    template_name = "list.html"
    model = BlogModel
    context_object_name = "blogList"

class BlogDetail(DetailView):
    template_name = "detail.html"
    model = BlogModel

class BlogCreate(CreateView):
    template_name = "create.html"
    model = BlogModel
    fields = (
        "title",
        "content",
        "category"
    )
    success_url = reverse_lazy("list")

class BlogUpdate(UpdateView):
    template_name = "update.html"
    model = BlogModel
    fields = (
        "title",
        "content",
        "category"
    )
    success_url = reverse_lazy("list")