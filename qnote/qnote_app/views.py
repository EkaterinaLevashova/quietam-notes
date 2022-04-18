from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from . import models


# return user_list
class UserListView(ListView):
    context_object_name = 'users'
    model = models.User


# return user
class UserDetailView(DetailView):
    context_object_name = 'user_detail'
    model = models.User
    template_name = 'qnote_app/user_detail.html'


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inject_me'] = 'BASIC INJECTION'
        return context
