from django.shortcuts import render,redirect
from .forms import TodoForm,RegistrationForm
from .models import TodoItem
from django.contrib.auth import login,authenticate,get_user_model,logout
from django.contrib.auth.decorators import login_required

User = get_user_model()

# Create your views here.
@login_required(login_url='login')
def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo_form.html', {'form': form})

@login_required(login_url='login')    
def retreive(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})

@login_required(login_url='login')
def update(request, id):
    todo = TodoItem.objects.get(pk=id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo_form.html', {'form': form})

@login_required(login_url='login')
def delete(request,id):
    todo = TodoItem.objects.get(pk=id)
    todo.delete()
    return redirect('/todo_list/')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todo_list')  
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
    
# def register_view(request):
#     reg_form = RegistrationForm()
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         email = request.POST.get('email')
#         User.objects.create_user(username=username,password=password,email=email)
#         return redirect('login')
#     return render(request, 'register.html', {'reg_form':reg_form})

def register_view(request): 
    if request.method == 'POST':
        reg_form = RegistrationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return redirect('login')
    else:
        reg_form = RegistrationForm()
    return render(request, 'register.html', {'reg_form':reg_form})

def logout_view(request):
    logout(request)
    return redirect('todo_list')
