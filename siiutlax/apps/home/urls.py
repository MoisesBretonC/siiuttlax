from django.urls import path

from . import views
from .views import welcome_view


app_name = "home"
urlpatterns = [
    path('home/', views.home, name='home'),
    path('', welcome_view, name='welcome'),
]
