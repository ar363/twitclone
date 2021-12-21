from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseRedirect

class UserIsAnonymousMixin(UserPassesTestMixin):
    def test_func(self):
        if not self.request.user.is_authenticated:
            return True
    
    def handle_no_permission(self):
        return HttpResponseRedirect('/home/')
    
    def get_redirect_field_name(self):
        return None