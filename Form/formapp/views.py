from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentRegistrationForm

# Create your views here.
def home(request):
    return HttpResponse("Welcome to Home")

def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'register.html',{'form': form})
    else:
        form = StudentRegistrationForm()

    return render(request, 'register.html', {'form': form})

