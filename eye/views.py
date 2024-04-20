from datetime import date

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def base_page(request):
    return render(request, 'base/base.html', {'base': 'base'})