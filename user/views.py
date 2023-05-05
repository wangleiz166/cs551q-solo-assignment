from django.shortcuts import render
from .models import User
import hashlib
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password,check_password 

def goto_index_view(request,url):
    # Redirect to example.com
    return HttpResponseRedirect(url)

def logout(request):
    response = goto_index_view(request,'/list')
    response.delete_cookie('username')
    response.delete_cookie('userid')
    return response


# Create your views here.
def login(request):
    if request.method == 'POST':
        # Get the user name and password entered by the user
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Find a user in the database
        try:
            user = User.objects.get(name=username)
        except User.DoesNotExist:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})

        # Check if the password matches
        if not check_password(password, user.password):
            error_message = 'Username or password does not match'
            return render(request, 'login.html', {'error_message': error_message})
        
        # Create a response object and set a cookie
        response = goto_index_view(request,'/list')
        
        user = User.objects.get(name=username)
        user_id = user.id

        response.set_cookie('userid', user_id, samesite='None', secure=True)
        response.set_cookie('username', username, samesite='None', secure=True)
        return response

    else:
        response = render(request, 'login.html')
        response.delete_cookie('username')
        response.delete_cookie('userid')
        return response
    

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']
        address = request.POST['address']
        zipcode = request.POST['zipcode']

        # Verify that the password is the same
        if password != confirm_password:
            return render(request, 'signup.html', {'error_message': '两次输入的密码不一致，请重新输入。'})

        # Check if the email is registered
        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error_message': '此电子邮件已被注册，请尝试使用其他电子邮件。'})
        
        # Check if the name is registered
        if User.objects.filter(name=name).exists():
            return render(request, 'signup.html', {'error_message': '此name已被注册，请尝试使用其他电子邮件。'})

        # Create new users and save them to the database
        hashed_password = make_password(password)
        new_user = User(name=name, email=email, password=hashed_password, address=address, zipcode=zipcode)
        new_user.save()

        # Redirect to other pages after successful registration, e.g. home page
        return render(request, 'signup_success.html')
    else:
        return render(request, 'signup.html', {'error_message': ''})
    