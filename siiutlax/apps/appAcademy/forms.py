from django.forms import Form, ModelForms

from .models import Professor, Student

class ProfessorForm(ModelForm):
    model = Professor
    fields = '__all__'

class StudentForm(ModelForm):
    model = Student 
    field = '__all__'