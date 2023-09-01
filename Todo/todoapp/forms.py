from .models import TodoItem 
from django import forms 
from django.contrib.auth import get_user_model

User = get_user_model()

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = '__all__'

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email']