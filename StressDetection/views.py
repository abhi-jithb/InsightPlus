from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {})

def logout(request):
    # Add logout logic here
    return render(request, 'index.html', {})

def UserLogin(request):
    return render(request, 'UserLogin.html', {})

def Community(request):
    return render(request, 'Community.html', {})

def UserRegister(request):
    form = UserCreationForm()  # Use Django's built-in UserCreationForm for user registration
    return render(request, 'UserRegistrations.html', {'form': form})

def user_login_check(request):
    if request.method == 'POST':
        login_id = request.POST.get('login_id')
        password = request.POST.get('password')
        user = authenticate(request, username=login_id, password=password)  # Use login_id and password variables
        if user is not None:
            # Authentication successful
            login(request, user)
            return HttpResponse("Login successful")
        else:
            # Authentication failed
            return HttpResponse("Login failed. Invalid credentials.")
    else:
        # Handle other HTTP methods (e.g., GET) if needed
        return HttpResponse("Method not allowed")


from django.contrib.auth import authenticate

# Assuming login_id is 'celes' and password is 'Celes@123'
login_id = 'celes'
password = 'Celes@123'

# Authenticate the user
user = authenticate(username=login_id, password=password)

if user is not None:
    # Authentication successful
    print("Login successful")
else:
    # Authentication failed
    print("Login failed. Invalid credentials.")

from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def user_login_check(request):
    if request.method == 'POST':
        login_id = request.POST.get('celes')  # Assuming 'loginname' is the name of the login ID field in your form
        password = request.POST.get('C')  # Assuming 'pswd' is the name of the password field in your form

        # Authenticate user
        user = authenticate(request, username=login_id, password=password)

        if user is not None:
            # User is authenticated, perform additional actions if needed
            login(request, user)  # Log the user in
            return HttpResponse('Login successful')  # You can return a success message or redirect to another page
        else:
            # Authentication failed
            return HttpResponse('Invalid login credentials')  # You can return an error message or redirect to the login page with an error
