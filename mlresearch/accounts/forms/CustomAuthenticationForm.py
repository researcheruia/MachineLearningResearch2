from django.contrib.auth.forms import AuthenticationForm
from django.forms import CharField, EmailField, EmailInput, PasswordInput
from django.utils.translation import gettext_lazy as _


class CustomAuthenticationForm(AuthenticationForm):
    username = EmailField(
        widget=EmailInput(
            attrs={
                "class": "form-control",
                "auto-focus": True
            }
        ),
        label=_("Usuario")
    )
    password = CharField(
        widget=PasswordInput(
            attrs={
                "class": "form-control",
            }
        ),
        label=_("Contraseña"),
        strip=False
    )