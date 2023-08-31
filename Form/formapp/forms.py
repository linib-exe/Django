from django import forms
from .models import Students

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name','email','phone']
