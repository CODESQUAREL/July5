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

        code_square_list = CODE_SQUARE.objects.all()

        return render(request, 'accountapp/CODE_SQUARE.html',
                      context = {'code_square_list': code_square_list})
    else:
        code_square_list = CODE_SQUARE.objects.all()
        return render(request, 'accountapp/CODE_SQUARE.html',
                      context = {'code_square_list': code_square_list})