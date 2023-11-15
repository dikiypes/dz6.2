from django.shortcuts import render
from django.http import HttpResponse


def index_catalog(request):
    return render(request, "catalog/index_catalog.html")


def contact(request):
    return render(request, "catalog/contact.html")
