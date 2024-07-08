from django.http import HttpResponse
from django.shortcuts import render
import pathlib

from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_view(request, *args, **kwargs):
    if (request.user.is_authenticated):
        print(request.user)
    return about_view(request, *args, **kwargs)


def about_view(request, *args, **kwargs):
    page_qs = PageVisit.objects.filter(path=request.path)
    qs = PageVisit.objects.all()
    try:
        percent = (page_qs.count()/qs.count())*100
    except:
        percent = 0
    my_title = "About Page"
    html_template = "home.html"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "percent": percent,
        "total_visit_count": qs.count(),
    }
    path = request.path
    print(path)
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)