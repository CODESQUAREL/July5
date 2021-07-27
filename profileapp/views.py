from django.shortcuts import render

# Create your views here.

# 로직 작성
from django.urls import reverse_lazy
from django.views.generic import CreateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:CODE_SQUARE')
    template_name = 'profileapp/create.html'


    #------> urls.py

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)