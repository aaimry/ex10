from django.urls import path

from api.views import accept_advertisement, reject_advertisement, get_token_view

app_name = 'api'

urlpatterns = [
    path('get-csrf-token/', get_token_view),
    path('advertisement/accept/', accept_advertisement, name='status_accept'),
    path('advertisement/reject/', reject_advertisement, name='status_reject')
]
