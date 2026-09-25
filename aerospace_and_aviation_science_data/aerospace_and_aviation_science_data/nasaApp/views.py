from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from nasaApp.services import ApodServices


def apod(request):
    # return HttpResponse("Hello, Geeks! Welcome to your first Django app.")
    result_list = ApodServices.get_apod_basic()
    context = {
        "result_list": result_list
    }
    return render(request, "apod.html", context)
    # return HttpResponse(template.render(),context)
