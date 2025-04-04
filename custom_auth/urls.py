from django.urls import path
from . import views

urlpatterns = [
    path('auth/register/', view=views.registration, name="register user"),
    path('auth/login/', view=views.login, name="login user"),
    path('auth/profile/', view=views.get_user_profile, name="protected user profile"),
    path('auth/profile/', view=views.patch_user_profile, name="protected updade profile"),
]