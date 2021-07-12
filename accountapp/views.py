from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def CODE_SQUARE(request):
    if request.method == "POST":

        temp = request.POST.get('input_text')

        return render(request, 'accountapp/CODE_SQUARE.html',
                      context = {'text': temp})
    else:
        return render(request, 'accountapp/CODE_SQUARE.html',
                      context = {'text': 'POST METHOD!'})