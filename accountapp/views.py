from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def CODE_SQUARE(request):
    if request.method == "POST":
        return render(request, 'accountapp/CODE_SQUARE.html',
                      context = {'text': 'POST METHOD!'})
    else:
        return render(request, 'accountapp/CODE_SQUARE.html',
                      context = {'text': 'POST METHOD!'})