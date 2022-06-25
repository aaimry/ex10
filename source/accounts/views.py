from django.contrib.auth import login
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.http import urlencode
from django.views.generic import CreateView, DetailView, UpdateView

from accounts.forms import UserRegistrationForm, UserUpdateForm
from accounts.models import MyUser
from webapp.forms import SearchForm
from webapp.models import Advertisement


class RegistrationView(CreateView):
    model = MyUser
    template_name = "accounts/registration.html"
    form_class = UserRegistrationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

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
    paginate_by = 9
    paginate_orphans = 0

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(Profile, self).get(request, **kwargs)

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        queryset = Advertisement.objects.all()
        if self.search_data:
            queryset = Advertisement.objects.filter(
                Q(title__icontains=self.search_data) |
                Q(description__icontains=self.search_data)
            )
        if self.request.user == user:
            context['advertisement'] = queryset.filter(Q(is_active=True) & Q(author=user))
        else:
            context['advertisement'] = queryset.filter(Q(author=user) & Q(status='published') & Q(is_active=True))
        context['search_form'] = self.form
        if self.search_data:
            context['query'] = urlencode({'search_value': self.search_data})
        return context
