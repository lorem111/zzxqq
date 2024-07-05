from django.http import HttpResponse
from django.shortcuts import render
import pathlib

from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    page_qs = PageVisit.objects.filter(path=request.path)
    qs = PageVisit.objects.all()
    my_title = "My Page"
    html_template = "home.html"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "percent": (page_qs.count()/qs.count())*100,
        "total_visit_count": qs.count(),
    }
    path = request.path
    print(path)
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)


def about_page_view(request, *args, **kwargs):
    my_title = "About Page"
    my_context = {
        "page_title": my_title
    }
    html_template = "about.html"
    return render(request, html_template, my_context)