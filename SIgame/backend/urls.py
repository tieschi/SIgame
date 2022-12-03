from django.urls import path
from backend import views

app_name = "backend"

urlpatterns = [
    path('login', views.LoginView),
    path('register', views.RegisterView),
    path('refresh-token', views.CookieTokenRefreshView.as_view()),
    path('logout', views.LogoutView),
    path('user', views.user),
]
