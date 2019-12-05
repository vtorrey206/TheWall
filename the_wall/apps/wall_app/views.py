from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import bcrypt
import datetime

def private(request):
    if request.session['userid'] == '':
        return redirect('/logreg')
    context = {
        'user':User.objects.get(id=request.session['userid']),
        'my_post':Post.objects.filter(creator_id=request.session['userid']), #this makes it dig a step deeper it gets the many to many key
        'my_comments': Comment.objects.filter(buzz__id=request.session['userid']), #might be exclude
    }
    print('*'*80)
    print('This page should not be loading')
    return render(request,'wall_app/private.html', context)


def public(request):
    # if request.session['userid'] == '':
    #     print('*'*80)
    #     print('Something went wrong at login or registration')
    #     return redirect('/logreg')
    context = {
        'user':User.objects.get(id=request.session['userid']),
        'my_post':Post.objects.filter(creator__id=request.session['userid']), #this makes it dig a step deeper it gets the many to many key
        'all_post':Post.objects.all(),
        'my_comments': Comment.objects.filter(commenter__id=request.session['userid']), #might be exclude
        'all_comments': Comment.objects.all()
    }
    print('*'*315)
    print('Main page loaded successfully!!!')
    return render(request,'wall_app/public.html', context)
    

def postprocess(request):
    if request.session['userid'] == '':
        return redirect('/logreg')
    errors = Post.objects.validate_post(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key) #make errors look good wont show up on both sides
        print('*'*80)
        print('Something went wrong with post')
        return redirect('/public')
    else:
        this_user = User.objects.get(id=request.session['userid'])
        make_post = Post.objects.create(content=request.POST['content'],creator=this_user)
        #this_post.creator.add(this_user)
        
        return redirect('/public')
    

def commentprocess(request):
    if request.session['userid'] == '':
        return redirect('/logreg')
    errors = Comment.objects.validate_comment(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key) #make errors look good wont show up on both sides
        print('*'*80)
        print('Something went wrong with comment')
        return redirect('/public')
    else:
        this_user = User.objects.get(id=request.session['userid'])
        this_post = Post.objects.get(id=request.POST['post_id']) #might need to be Post_id or Buzz_id
        make_comment = Comment.objects.create(c_content=request.POST['c_content'], buzz=this_post, commenter=this_user)
        #this_post.creator.add(this_user)
        
        return redirect('/public')


def deletepost(request, post_id):
    if request.session['userid'] == '':
        return redirect('/logreg')
    
    this_post = Post.objects.get(id=int(post_id))
    if this_post.creator.id != request.session['userid']:
        print('Something went wrong with deleting post')
        return redirect('/public')
    else:
        this_post.delete()
        return redirect('/public')

def deletecomment(request, comm_id):
    if request.session['userid'] == '':
        return redirect('/logreg')
    
    this_comment = Comment.objects.get(id=int(comm_id))
    if this_comment.creator.id != request.session['userid']:
        print('Something went wrong with deleting comment')
        return redirect('/public')
    else:
        this_comment.delete()
        return redirect('/public')


def logout(request):
    request.session.flush()
    return redirect('/logreg/')


    