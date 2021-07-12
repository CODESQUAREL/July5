from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import CODE_SQUARE


def code_square(request):
    if request.method == "POST":

        temp = request.POST.get('input_text')

        new_code_square = CODE_SQUARE()
        new_code_square.text = temp
        new_code_square.save()

        return render(request, 'accountapp/CODE_SQUARE.html',
                      context = {'new_code_square': new_code_square})
    else:
        return render(request, 'accountapp/CODE_SQUARE.html',
                      context = {'text': 'GET METHOD!'})