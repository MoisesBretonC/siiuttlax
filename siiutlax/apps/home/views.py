from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home/home.html')

def welcome_view(request):
    return render(request, 'welcome/welcome.html')
