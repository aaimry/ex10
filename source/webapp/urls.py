from django.urls import path

from webapp.views import AdvertisementListView, AdvertisementDetailView, AdvertisementUpdateView, \
    AdvertisementDeleteView, AdvertisementCreateView

app_name = 'webapp'

urlpatterns = [
    path('', AdvertisementListView.as_view(), name='advertisement_list'),
    path('ad/create', AdvertisementCreateView.as_view(),name='advertisement_create'),
    path('ad/detail/<int:pk>', AdvertisementDetailView.as_view(), name='advertisement_detail'),
    path('ad/update/<int:pk>', AdvertisementUpdateView.as_view(), name='advertisement_update'),
    path('ad/delete/<int:pk>', AdvertisementDeleteView.as_view(), name='advertisement_delete')
]
