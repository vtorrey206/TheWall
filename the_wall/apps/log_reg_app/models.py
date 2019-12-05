from django.db import models
#from apps.wall_app.models import Post, Comment
import re
import bcrypt
import datetime
#import relativedelta
# first name last name so on asre attributes
# when you set your chrfield to a number it takes up that amout of space in the data base so if its 100 no matter what the name is it takes up that space 
# Each form needs it own method if you try to have validations that are not there you will get a error


# dont forget to import models
class UserManager(models.Manager): #its post because our form is doing a post method
    def validate_registration(self,postData):
        errors = {}
        try:
            if len(postData['first_name']) < 3 or str.isalpha(postData['first_name']) ==False:
                errors['first_name'] = 'First name must contain more than 3 charactor letters only'

            if len(postData['last_name']) < 3 or str.isalpha(postData['last_name']) ==False:
                errors['last_name'] = 'Last name must contain more than 3 charactor letters only'
                # dont forget to import regex like import re 
            

            EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            if not EMAIL_REGEX.match(postData['email']):
                errors['email'] = 'Invalid email address'
                # .match is a python built in also elif is there because there is no need to check another if, if it stops at if
            elif EMAIL_REGEX.match(postData['email']):
                # flat=true will give you a literal list of values only without this it would of gave the key aswell 
                existing_emails = User.objects.values_list('email',flat=True)
                if postData['email'] in existing_emails:
                    errors['email'] = 'This email is already being used'
            
            if len(postData['password']) < 8:
                errors['password'] = 'Password must be atleast 8 charactors long please'
                # the name has to match what you put in your html so if you have confirm it needs to be confirm 
            if postData['password'] != postData['confirm']:
                errors['confirm'] = 'Passwords do not match'
        except:
            errors['general'] = 'Something went wront please try again'
        return errors


    def validate_login(self,postData):
        errors = {}
        try:
            if postData['email'] =='':
                errors['log_email'] = 'Email cant be empty'
            elif postData['email'] != '':
                existing_emails = User.objects.values_list('email',flat=True)
                if postData['email'] not in existing_emails:
                    # each error needs a unique key or it will throw both error on register and log in unique key for every location
                    errors['log_email'] = 'This email is not in out system have you registred?'


            if postData['password'] =='':
                errors['log_password'] = 'Password cant be empty'
            # dont forget to import bcrypt
            elif postData['password'] != '':
                existing_user = User.objects.filter(email = ['email'])
                if not bcrypt.checkpw(postData['password'].encode(), existing_user[0].password.encode()):
                    # you need to call it log email so they dont know that the password is the issue to secure the password 
                    errors['log_email'] = 'Email and or password dont match'
        except:
            errors['general'] = 'Something went wront please try again'
        return errors



class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    DOB = models.DateTimeField()
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()