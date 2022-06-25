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
    paginate_by = 10
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


class AdvertisementCreateView(CreateView):
    model = Advertisement
    form_class = AdvertisementCreateForm
    template_name = 'webapp/advertisement_create.html'

    def form_valid(self, form):
        advertisement = form.save(commit=False)
        advertisement.author = self.request.user
        advertisement.save()
        return redirect('webapp:advertisement_list')


class AdvertisementUpdateView(UpdateView):
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


class AdvertisementDeleteView(DeleteView):
    model = Advertisement
    template_name = 'webapp/advertisement_delete.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(Q(status='published') & Q(is_active=True))
        return queryset

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.adv_delete()
        return redirect('webapp:advertisement_list')
