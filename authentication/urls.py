from django.views.decorators.csrf import csrf_exempt

from .views import RegisterView, UsernameValidationView, EmailValidationView, VerificationView, LoginView, LogoutView
from django.urls import path

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()),
         name="validate-username"),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()), name="validate-email"),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name="activate"),
    path('logout/', LogoutView.as_view(), name='logout'),
]
