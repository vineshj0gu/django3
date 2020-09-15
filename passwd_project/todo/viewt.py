from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import  IntegrityError
from .forms import TodoFrom
from .models import Todo
from django.utils import timezone



# Create your views here.
@login_required
def create(request):
    if request.method == 'GET':
        return render(request, 'todo/create.html',{'form':TodoFrom()} )
    else:
        try:
                form = TodoFrom(request.POST)
                newtodo = form.save(commit=False)
                newtodo.user = request.user
                newtodo.save()
                return redirect('current')
        except ValueError:
            return render(request, 'todo/create.html',{'form':TodoFrom(), 'error': 'please check your data '} )


def out(request):
    return render(request, 'todo/out.html' )

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signup.html',{'form':UserCreationForm()} )
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('current')
            except IntegrityError:
                return render(request, 'todo/signup.html',{'form':UserCreationForm(),'error':'pls try diff username'} )
        else:
            return render(request, 'todo/signup.html',{'form':UserCreationForm(),'error':'passwods didnot match'} )

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/login.html',{'form':AuthenticationForm()} )
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todo/login.html',{'form':AuthenticationForm(),'error':'wrong user or passwd'} )
        else:
            login(request, user)
            return redirect('current')



def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return   redirect('out')
@login_required
def current(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'todo/current.html', {'todo':todos})
@login_required
def alldone(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=False).order_by('datecompleted')
    return render(request, 'todo/alldone.html', {'todo':todos})
@login_required
def viewtodo(request, todo_pk):
    todos = get_object_or_404(Todo, pk=todo_pk)
    if request.method == 'GET':
        form = TodoFrom(instance=todos)
        return render(request, 'todo/viewtodo.html', {'todo':todos, 'form':form})
    else:
        try:
            form = TodoFrom(request.POST, instance=todos)
            form.save()
            return redirect('current')
        except ValueError:
            return render(request, 'todo/viewtodo.html',  {'todo':todos, 'form':form, 'error': 'bad info'})
@login_required
def completetodo(request, todo_pk):
    todos =  get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todos.datecompleted = timezone.now()
        time = timezone.now()
        print(time)
        todos.save()
        return redirect('current')
@login_required
def deletetodo(request, todo_pk):
    todos =  get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todos.datecompleted = timezone.now()
        time = timezone.now()
        print(time)
        todos.delete()
        return redirect('current')


@login_required
def todo(request):
    return render(request, 'todo/todo.html' )
