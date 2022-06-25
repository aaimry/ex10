from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import RegistrationView, Profile, UserUpdateView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name="../templates/accounts/login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('profile/<int:pk>', Profile.as_view(), name='profile'),
    path('update/user/<int:pk>', UserUpdateView.as_view(), name='update_user')
]
