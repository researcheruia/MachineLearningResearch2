from django.contrib.auth.views import LoginView


from ..forms import CustomAuthenticationForm


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
