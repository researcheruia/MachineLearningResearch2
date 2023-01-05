from django.contrib.auth.forms import UserCreationForm
from django.forms import CharField, EmailInput, DateInput, PasswordInput, TextInput
from django.utils.translation import gettext_lazy as _


from ..models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    password1 = CharField(
        label=_("Contraseña"),
        strip=False,
        widget=PasswordInput(attrs={"class": "form-control"}),
    )
    password2 = CharField(
        label=_("Contraseña (otra vez)"),
        strip=False,
        widget=PasswordInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "birth_date",
        )
        labels = {
            "username": "Usuario",
            "first_name": "Nombre",
            "last_name": "Apellido",
            "email": "Correo Electrónico",
            "birth_date": "Fecha de Nacimiento",
        }
        widgets = {
            "username": TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "first_name": TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "last_name": TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "email": EmailInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "birth_date": DateInput(
                attrs={
                    "class": "form-control"
                }
            ),
        }
