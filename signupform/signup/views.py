#if possible -email confirmation


from django.shortcuts import render , redirect
from .forms import SignupForm
from django.contrib.auth import authenticate , login , logout
#import messages
from .models import User

def home(request):
    return render(request , 'home.html')

def profile(request):
    
    return render(request , "profile.html")

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request , 'signup.html',{
        'form' : form
    })

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request , username = username , password = password)
        if user is not None:
            login(request , user)
            #messages.success(request , 'you are logged in')
        
    return render(request , 'login.html')


#change password
def change_password(request):
    if request.method == "POST":
        pass

# forgot password
def forgot_passward(request):
    pass