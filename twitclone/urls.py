from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing_page'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('logout/', views.logout_view, name='logout'),

    path('home/', views.homepage, name='home_page'),
    path('search/', views.searchpage, name='search_page'),
    path('home/_frame/feed/', views.feed_frame, name='feed_frame'),
    path('home/_frame/search/', views.search_frame, name='search_frame'),
    path('home/me/', views.profile, name='profile_frame'),

    path('tweet/add/', views.create_tweet, name='frame-add_tweet')
]