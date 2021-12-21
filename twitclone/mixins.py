from django.contrib.auth.mixins import UserPassesTestMixin

class UserIsAnonymousMixin(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_authenticated
    
    def get_login_url(self):
        return '/home/'
    
    def get_redirect_field_name(self):
        return None