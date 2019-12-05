from django.shortcuts import render,redirect
from apps.wall_app.models import Post, Comment
from apps.log_reg_app.models import User
from django.contrib import messages
import bcrypt
import datetime



def log_reg(request):
    request.session.flush()
    if 'userid' not in request.session:
        request.session['userid'] = ''
        return render(request, 'log_reg_app/log_reg.html')

def register(request):
    if request.method != 'POST':
        return redirect('/logreg')
    errors = User.objects.validate_registration(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key) #make errors look good wont show up on both sides
        print('*'*315)
        print('Errors redirected User back to login page')    
        return redirect('/logreg')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], DOB = request.POST['DOB'], email = request.POST['email'], password = pw_hash)
        request.session['userid'] = user.id
        return redirect('/public')

def login(request):
    if request.method != 'POST':
        return redirect('/logreg')
    errors = User.objects.validate_login(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key) #make errors look good wont show up on both sides
        print('*'*315)
        print('Login was not successful!!!!')
        return redirect('/logreg')
    else:
        user = User.objects.get(email = request.POST['email'])
        request.session['userid'] = user.id
        print('*'*80)
        print('login successful!')
        print('errors')
        return redirect('/public')

def logout(request):
    request.session.flush()
    return redirect('/logreg/')
