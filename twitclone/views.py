from django.views.generic import TemplateView

class LandingPageView(TemplateView):
    template_name = 'twitclone/landing_page.html'