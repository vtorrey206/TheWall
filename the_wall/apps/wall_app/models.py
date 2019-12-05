from django.db import models
from apps.log_reg_app.models import *
#import re
#import bcrypt
#import datetime


class PostManager(models.Manager):
    def validate_post(self,postData):
        errors = {}
        try:
            if len(postData['content']) < 1:
                errors['content'] = 'Post can not be empty'
        except:
            errors['general'] = 'Something went wrong please try again'
        return errors

    


class CommentManager(models.Manager):
    def validate_comment(self,postData):
        errors = {}
        try:
            if len(postData['c_content']) < 1:
                errors['c_content'] = 'Comments can not be empty' 
        except:
            errors['general'] = 'Something went wrong please try again'
        return errors
            



class Post(models.Model):
    content = models.TextField()
    creator = models.ForeignKey(User, related_name='post_created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostManager()

class Comment(models.Model):
    c_content = models.TextField()
    buzz = models.ForeignKey(Post, related_name='comments_for_post')
    commenter = models.ForeignKey(User, related_name='comment_made')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()
    

