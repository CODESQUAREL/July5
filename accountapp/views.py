from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorator import account_ownership_required
from accountapp.forms import AccountCreationForm
from accountapp.models import CODE_SQUARE
from articleapp.models import Article


@login_required#(login_url:reverse_lazy('accountapp:login'))
def code_square(request):
    if request.method == "POST":

        temp = request.POST.get('input_text')

        new_code_square = CODE_SQUARE()
        new_code_square.text = temp
        new_code_square.save()

        # code_square_list = CODE_SQUARE.objects.all()

        return HttpResponseRedirect(reverse('accountapp:CODE_SQUARE'))
    else:
        code_square_list = CODE_SQUARE.objects.all()
        return render(request, 'accountapp/CODE_SQUARE.html',
                      context = {'code_square_list': code_square_list})



class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:CODE_SQUARE')
    template_name = 'accountapp/create.html'

# 회원가입 로직 끝
# 라우팅 : 어떤 주소로 접근해야 회원가입 페이지로 갈지를 작성해줘야함. accountapp/urls.py에 path구문 작성함

# ---------------------------------------

class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    paginate_by = 20

    def get_context_data(self, **kwargs):
        article_list = Article.objects.filter(writer=self.object) # self.object = target_user
        return super().get_context_data(object_list=article_list, **kwargs)

# 이거 작성하고 urls 에서 라우팅하는 것을 꼭 작성해줘야함

has_ownership = [login_required, account_ownership_required]
#method_decorator는 리스ㅌ 형태도 불러올 수 있다. (기능 두가지를 불러올 수 있는 것)

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    template_name = 'accountapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.pk})

    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and self.get_object() == request.user: #self.get_object는 pk(target_user)로 이해한다.
    #         return super().get(request, *args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()
    #
    # def post(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and self.get_object() == request.user:
    #         return super().post(request, *args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:CODE_SQUARE')
    template_name = 'accountapp/delete.html'

    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and self.get_object() == request.user:
    #         return super().get(request, *args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()
    #
    # def post(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and self.get_object() == request.user:
    #         return super().post(request, *args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()
    #
