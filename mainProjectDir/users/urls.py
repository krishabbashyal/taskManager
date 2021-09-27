from django.urls import path
from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register/", views.UserView.as_view(), name = "register"),
    path("login/", auth_views.LoginView.as_view(template_name = 'users/loginPage.html'), name = "login"),
]
