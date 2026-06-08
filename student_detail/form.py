from django import forms
from .models import Student_d

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student_d
        fields = '__all__'