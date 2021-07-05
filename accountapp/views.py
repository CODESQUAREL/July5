from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def CODE_SQUARE(request):
    return render(request, 'accountapp/CODE_SQUARE.html')