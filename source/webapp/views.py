from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db.models import Q
from django.utils.http import urlencode
from django.shortcuts import redirect

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import SearchForm, AdvertisementCreateForm, AdvertisementUpdateForm
from webapp.models import Advertisement


class AdvertisementListView(ListView):
    template_name = 'webapp/advertisement_list.html'
    model = Advertisement
    context_object_name = 'advertisement'
    ordering = ('-created_at')
    paginate_by = 1
    paginate_orphans = 0

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(AdvertisementListView, self).get(request, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(Q(status='published') & Q(is_active=True))

        if self.search_data:
            queryset = queryset.filter(
                Q(title__icontains=self.search_data) |
                Q(description__icontains=self.search_data)
            )
        return queryset

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form
        if self.search_data:
            context['query'] = urlencode({'search_value': self.search_data})
        return context


class AdvertisementDetailView(DetailView):
    model = Advertisement
    template_name = 'webapp/advertisement_detail.html'
    context_object_name = 'advertisement'


class AdvertisementCreateView(LoginRequiredMixin, CreateView):
    model = Advertisement
    form_class = AdvertisementCreateForm
    template_name = 'webapp/advertisement_create.html'

    def form_valid(self, form):
        advertisement = form.save(commit=False)
        advertisement.author = self.request.user
        advertisement.save()
        return redirect('webapp:advertisement_list')


class AdvertisementUpdateView(PermissionRequiredMixin, UpdateView):
    model = Advertisement
    form_class = AdvertisementUpdateForm
    template_name = 'webapp/advertisement_update.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(Q(status='published') & Q(is_active=True))
        return queryset

    def form_valid(self, form):
        advertisement = form.save(commit=False)
        advertisement.update_time()
        advertisement.save()
        return redirect(self.success_url)

    def has_permission(self):
        return self.get_object().author == self.request.user


class AdvertisementDeleteView(PermissionRequiredMixin, DeleteView):
    model = Advertisement
    template_name = 'webapp/advertisement_delete.html'
    context_object_name = 'advertisement'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(Q(status='published') & Q(is_active=True))
        return queryset

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.adv_delete()
        return redirect('webapp:advertisement_list')

    def has_permission(self):
        return self.get_object().author == self.request.user


class AdvertisementToModerateView(PermissionRequiredMixin, ListView):
    model = Advertisement
    template_name = 'moderator/list.html'
    ordering = ('-created_at')
    paginate_by = 2
    paginate_orphans = 0

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(status="to_moderate").exclude(is_active=False)
        if self.search_data:
            queryset = queryset.filter(
                Q(title__icontains=self.search_data) |
                Q(description__icontains=self.search_data)
            )
        return queryset

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form
        if self.search_data:
            context['query'] = urlencode({'search_value': self.search_data})
            return context
        context['advertisement_list'] = self.get_queryset()
        return context

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(AdvertisementToModerateView, self).get(request, **kwargs)

    def has_permission(self):
        return self.request.user.is_staff


class AdvertisementApproveView(PermissionRequiredMixin, DetailView):
    model = Advertisement
    template_name = 'moderator/advertisement_approve.html'
    context_object_name = 'advertisement'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(status='to_moderate').exclude(is_active=False)
        return queryset

    def has_permission(self):
        return self.request.user.is_staff
