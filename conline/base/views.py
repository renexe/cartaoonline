# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return HttpResponse('<html><body>Olá Django</body></html>', content_type='text/html')
