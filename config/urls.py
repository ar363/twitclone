from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('socialauth/', include('social_django.urls', namespace='social')),
    path('', include('twitclone.urls')),
]
