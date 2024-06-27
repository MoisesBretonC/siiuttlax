from django.urls import path
from . import views


app_period = "period"
urlpatterns = {
    path('',views.Period,name='period')
}