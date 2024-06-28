from django.shortcuts import render

# Create your views here.

def Academy(request):
    return render(request, 'Academy/Academy.html')