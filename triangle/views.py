from django.shortcuts import render


def index(request):
    return render(request, "triangle/new_site.html")
