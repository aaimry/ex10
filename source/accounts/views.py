from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView

from accounts.forms import UserRegistrationForm, UserUpdateForm
from accounts.models import MyUser


class RegistrationView(CreateView):
    model = MyUser
    template_name = "accounts/registration.html"
    form_class = UserRegistrationForm

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('webapp:advertisement_list')
        return next_url


class UserUpdateView(UpdateView):
    model = MyUser
    template_name = 'accounts/update_profile.html'
    context_object_name = "user_object"
    form_class = UserUpdateForm


class Profile(DetailView):
    model = MyUser
    template_name = 'accounts/profile.html'
    context_object_name = 'user_object'
