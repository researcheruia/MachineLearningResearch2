from django.contrib.auth.forms import UserChangeForm
from django.forms import EmailInput, DateInput, PasswordInput, TextInput
from ..models import CustomUser


class CustomUserChangeForm(UserChangeForm):
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
            "password1": "Ingrese una Contraseña",
            "password2": "Repita la Contraseña"

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
            "password1": PasswordInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "password2": PasswordInput(
                attrs={
                    "class": "form-control"
                }
            )
        }
