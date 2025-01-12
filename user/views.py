from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CommonsUser
#@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return render(request, 'user/register.html')
        if CommonsUser.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken!")
            return render(request, 'user/register.html')
        if CommonsUser.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered!")
            return render(request, 'user/register.html')
        user = CommonsUser(
            username=username,
            email=email,
            password=make_password(password1)  
        )
        user.save()
        print(f"Authenticated user: {user}")
        login(request, user)
        messages.success(request, "Registration successful!")
        return redirect('/sms/dashboard/')  
    return render(request, 'user/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Username: {username}, Password: {password}")  # Debugging
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(f"Authenticated user: {user}")  # Debugging
            login(request, user)
            return redirect('/sms/dashboard/')  # Redirect to dashboard
        else:
            messages.error(request, "Invalid username or password.")
            print("Authentication failed.")  # Debugging output
    return render(request, 'user/login.html')
    
def logout_view(request):
    logout(request)
    return redirect('login')  
