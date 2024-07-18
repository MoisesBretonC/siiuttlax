from django.shortcuts import render

# Create your views here.

from .forms import ProfesorForm,StudentForm

def create_professor(request):
    form = ProfesorForm()
    return render(request,
                  'academy/create_professor.html',
                  {'form':form})
    
def create_student(request):
    form = StudentForm()
    return render(request,
                  'academy/create_student.html',
                  {'form':form})
    
    
