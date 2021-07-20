from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountCreationForm
from accountapp.models import CODE_SQUARE


def code_square(request):
    if request.user.is_authenticated:
        if request.method == "POST":

            temp = request.POST.get('input_text')

            new_code_square = CODE_SQUARE()
            new_code_square.text = temp
            new_code_square.save()

            code_square_list = CODE_SQUARE.objects.all()

            return HttpResponseRedirect(reverse('accountapp:CODE_SQUARE'))
        else:
            code_square_list = CODE_SQUARE.objects.all()
            return render(request, 'accountapp/CODE_SQUARE.html',
                          context = {'code_square_list': code_square_list})
    else:
        return HttpResponseRedirect(reverse('accountapp:login'))


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:CODE_SQUARE')
    template_name = 'accountapp/create.html'

# 회원가입 로직 끝
# 라우팅 : 어떤 주소로 접근해야 회원가입 페이지로 갈지를 작성해줘야함. accountapp/urls.py에 path구문 작성함

# ---------------------------------------

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

# 이거 작성하고 urls 에서 라우팅하는 것을 꼭 작성해줘야함

class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:CODE_SQUARE')
    template_name = 'accountapp/update.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))



class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:CODE_SQUARE')
    template_name = 'accountapp/delete.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))

