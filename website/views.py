# Create your views here.
from django.shortcuts import render
# from django.contrib.auth.decorators import login_required


# @login_required(login_url='/login')
def home(request):
    return render(request, "landing.html")


def region(request):
    return render(request, "region.html")


def city(request):
    return render(request, "city.html")


def club(request):
    return render(request, "club.html")


def campo(request):
    return render(request, "campo.html")


def flora(request):
    return render(request, "flora.html")


def fauna(request):
    return render(request, "fauna.html")
