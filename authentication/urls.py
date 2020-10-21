from django.views.decorators.csrf import csrf_exempt

from .views import RegisterView, UsernameValidationView, EmailValidationView
from django.urls import path

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()),
         name="validate-username"),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()), name="validate-email")
]
