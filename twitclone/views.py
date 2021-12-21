from django.contrib.auth import REDIRECT_FIELD_NAME
from django.views.generic import TemplateView, FormView

from .forms import SignupForm, LoginForm
from .mixins import UserIsAnonymousMixin

class LandingPageView(TemplateView):
    template_name = 'twitclone/landing_page.html'

class LoginView(UserIsAnonymousMixin, FormView):
    template_name = 'twitclone/login.html'
    form_class = LoginForm
    success_url = '/home/'

class SignupView(UserIsAnonymousMixin, FormView):
    template_name = 'twitclone/signup.html'
    form_class = SignupForm
    success_url = '/home/'