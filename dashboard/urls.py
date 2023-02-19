from django.urls import path

from .views import DashboardView


urlpatterns = [
    path('post/', DashboardView.as_view(), name='dashboard'),
]
