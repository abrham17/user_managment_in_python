from django.shortcuts import render, redirect
from .forms import SignupForm , UserUpdateForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
import random
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
# Remove settings configuration from here; they are now in settings.py

verification_codes = {}

def home(request):
    return render(request, 'home.html')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(username=request.user.username)
    return render(request, 'profile.html', {'user': user})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            code = random.randint(100000, 999999)
            verification_codes[email] = code
            send_mail(
                'Password Reset Verification Code',
                f'Your verification code is: {code}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False
            )
            messages.success(request, 'A verification code has been sent to your email.')
            return redirect('verify_code', email=email)
        else:
            messages.error(request, 'No account found with this email address.')
    return render(request, 'forgot_password.html')
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  
            user.save()
            code = random.randint(100000, 999999)
            verification_codes[user.email] = code
            send_mail(
                'Email Confirmation Code',
                f'Your confirmation code is: {code}',
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False
            )
            messages.success(request, 'Please confirm your email address to complete registration.')
            return redirect('verify_signup_code', email=user.email)
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def verify_signup_code(request, email):
    if request.method == 'POST':
        code = request.POST.get('code')
        if verification_codes.get(email) == int(code):
            try:
                user = User.objects.get(email=email)
                user.is_active = True
                user.save()
                del verification_codes[email]
                messages.success(request, 'Email verified. You can now log in.')
                return redirect('login')
            except User.DoesNotExist:
                messages.error(request, 'User not found.')
                return redirect('signup')
        messages.error(request, 'Invalid verification code.')
    
    # GET request or invalid code
    return render(request, 'verify_code.html', {
        'email': email,
        'purpose': 'signup'
    })

def verify_code(request, email):
    if request.method == 'POST':
        code = request.POST.get('code')
        if verification_codes.get(email) == int(code):
            del verification_codes[email]
            messages.success(request, 'Verification successful. Please update your password.')
            return redirect('update_password', email=email)
        else:
            messages.error(request, 'Invalid verification code.')
    return render(request, 'verify_code.html', {'email': email})

def update_password(request, email):
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            users = User.objects.filter(email=email)
            for user in users:
                user.set_password(password1)
                user.save()
            messages.success(request, 'Password updated successfully. You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')
    return render(request, 'update_password.html', {'email': email})
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    return redirect('profile')
def update_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
        else:
            # Handle form errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.title()}: {error}")
    return redirect('profile')
