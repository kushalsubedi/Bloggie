from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def register_user(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print('form is not valid')
    context = {'form':form}
    return render(request,'registration/register.html',context)

def login_user(request):
    next = request.GET.get('next',"/")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(next)
        else:
            print('user is not authenticated')
    context = {}
    return render(request,'registration/login.html',context)



def logout_user(request):
    next=request.POST.get('next','/')
    logout(request)
    return redirect(next)
