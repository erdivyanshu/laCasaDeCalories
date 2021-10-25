from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from home.models import Contact, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    context = {"home": "active"}
    return render(request,'index.html', context)

def contact(request):
    context = {"contact": "active"}
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        need = request.POST['need']
        content = request.POST['content']

        if len(email) < 3 or len(content) < 4:
            messages.error(request, "Please fill the form correctly!")
        else:
            contact = Contact(name=name,email=email,need=need,content=content)
            contact.save()
            messages.success(request, "Your message has been sent!")
            messages.warning(request, "Admin will respond back soon!")
    return render(request, 'contact.html', context)

def catalog(request):
    context = {"home": "active"}
    return render(request, 'index.html', context)

def signup(request):
    if request.method == "POST":
        # Get the post parameters
        firstname = request.POST['firstname']
        username = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        # weights = request.POST['weights']
        gender = request.POST['gender']
        address = request.POST['address']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneous input
        if len(username) > 10:
            messages.error(request, "Username must be under 10 character")
            return redirect('home')
        if not username.isalnum():
            messages.error(request, "Username can be only alphanemuric")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, "Password do not match")
            return redirect('home')
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.name = firstname
        myuser.save()
        messages.success(request, " You are succesfully SignUP!")
        return redirect('home')
    else:
        #  messages.error(request, "Input Correct Credentials!")
        #return HttpResponse("404 - Not found")
        return render(request, 'signup.html')
              
    return render(request, 'signup.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            messages.success(request, " You are succesfully Logged-In on laCasaDeCalories Portal")
            return redirect('home')

        else:
            messages.error(request, "Input Correct Credentials!")
            return render(request, 'login.html')
    return render(request, 'login.html')

#    return HttpResponse("404 - Not found")
def logoutUser(request):
    logout(request)
    messages.success(request, "You are Successfully Logged-Out!")
    return redirect('home')

def profile(request):
    context = {"profile": "active"}
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request,'profile.html', context)
