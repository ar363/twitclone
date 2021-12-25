from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.db.models import Q

from twitclone.models import Tweet, User

from .forms import ProfileForm, SignupForm, LoginForm, TweetCreateForm
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
def searchpage(request):
    if 'q' not in request.GET:
        return HttpResponseNotFound("No search term provided: Page not found")
    
    return render(request, 'twitclone/home/index.html', {
        'q': request.GET['q']
    })

@login_required(login_url='/login/')
def feed_frame(request):
    return render(request, 'twitclone/home/frames/feed_frame.html', {
        'tweets': Tweet.objects.all().order_by('-created_at')
    })

@login_required(login_url='/login/')
def search_frame(request):
    q = request.GET['q']
    return render(request, 'twitclone/home/frames/feed_frame.html', {
        'tweets': Tweet.objects.all().filter(
            Q(text__icontains=q) |
            Q(author__username__icontains=q)
            ).order_by('-created_at'),
        'q': q
    })

@login_required(login_url='/login/')
def profile(request):
    if request.method == 'GET':
        return render(request, 'twitclone/home/profile.html', {
            'form': ProfileForm(initial={
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'username': request.user.username,
                'profile_picture': request.user.profile_picture,
                'bio': request.user.bio,
            })
        })
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            u = User.objects.get(id=request.user.id)
            for k in form.data:
                setattr(u, k, form.data[k])
            if 'profile_picture' in request.FILES:
                u.profile_picture = request.FILES['profile_picture']
            u.save()
        else:
            print(form.errors)
        
        return HttpResponseRedirect('/home/me/')

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
