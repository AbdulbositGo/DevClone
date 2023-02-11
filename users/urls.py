from django.urls import path

from .views import RegisterView, LoginView, LogoutView, ProfileView, SettingsView, DashboardView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('settings/', SettingsView.as_view(), name='settings'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('<str:username>/', ProfileView.as_view(), name='profile'),
]
