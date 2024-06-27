from django.urls import path
from . import views


app_career ="career"
urlpatterns ={
        path('',views.Career,name='career')
    }