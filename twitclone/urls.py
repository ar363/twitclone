from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing_page'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('logout/', views.logout_view, name='logout'),

    path('home/', views.homepage, name='home_page'),
]