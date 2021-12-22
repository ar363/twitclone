from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth import logout

from twitclone.models import Tweet

from .forms import SignupForm, LoginForm, TweetCreateForm
from .mixins import UserIsAnonymousMixin
from .generic import FormView


class LandingPageView(UserIsAnonymousMixin, TemplateView):
    template_name = 'twitclone/landing_page.html'


class LoginView(UserIsAnonymousMixin, FormView):
    template_name = 'twitclone/login.html'
    form_class = LoginForm
    success_url = '/home/'

    def form_valid(self, form):
        username = self.request.POST['username']
        password = self.request.POST['password']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect(self.success_url)


class SignupView(UserIsAnonymousMixin, FormView):
    template_name = 'twitclone/signup.html'
    form_class = SignupForm
    success_url = '/home/'

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect(self.success_url)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url='/login/')
def homepage(request):
    return render(request, 'twitclone/home/index.html', {})

@login_required(login_url='/login/')
def feed_frame(request):
    return render(request, 'twitclone/home/frames/feed_frame.html', {
        'tweets': Tweet.objects.all().order_by('-created_at')
    })


@login_required(login_url='/login/')
def create_tweet(request):
    if request.method == 'POST':
        form = TweetCreateForm(request.POST)
        if form.is_valid():
            t = form.save(commit=False)
            t.author = request.user
            t.save()
            return HttpResponseRedirect('/home/_frame/feed/')
        else:
            return HttpResponseRedirect('/home/_frame/feed/')
