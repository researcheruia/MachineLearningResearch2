from django.urls import path


from .views import CustomLoginView, SignUpPageView


urlpatterns = [
    # Inicio de sesión
    path("login/", CustomLoginView.as_view(), name="login"),
    # Registro de usuario
    path("signup/", SignUpPageView.as_view(), name="signup"),

]
