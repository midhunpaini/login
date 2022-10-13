from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.cache import cache_control

# Create your views here.

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):    
    if 'username' in request.session:             
       return render(request, "home.html")             
    return redirect('signin') 
  
   
@cache_control(no_cache=True, must_revalidate=True, no_store=True) 
def signin(request):
    if 'username' in request.session:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        user = authenticate(username=username, password=pass1)   
       
        if user is not None:
            request.session['username'] = username
            login(request, user)                     
            return redirect('home')
    
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('home')   
    
    return render(request, "signin.html")



    
def signout(request):
    if 'username' in request.session:
        request.session.flush()    
    messages.success(request, "Signed out Successfully!")
    return redirect('home')
   
        
   