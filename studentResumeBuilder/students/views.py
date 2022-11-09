from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('resume-form')
        else:
            messages.success(request, ("There was an Error logging in.. please try again"))
            return redirect('login')
    else:
        return render(request, 'students/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("Logged out successfully"))
    return redirect('landing-page')

def register_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            messages.success(request, ("Registration Successful"))
            return redirect('login')
        else:
            messages.error(request, ("An error occured while registering"))
            return render(request, 'students/register.html', {
                'form': form
            })
    else:
        form = UserCreationForm()
        return render(request, 'students/register.html', {
            'form': form
        })