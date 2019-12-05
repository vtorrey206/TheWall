from django.conf.urls import url
from . import views
from .models import User

                    
urlpatterns = [
     url(r'^private$', views.private), # This is the home page for logged in users  this will be rendering that page
     url(r'^public$', views.public), # This is the home page for logged in users  this will be rendering that page
     url(r'^postprocess$', views.postprocess), #This is the process for making a post this will redirect to the public or private page
     url(r'^commentprocess$', views.commentprocess), #This is the process for making a comment this will redirect to the public or private page
     url(r'^deletepost/(?P<post_id>\d+)$', views.deletepost), #This is the process for deleting a post this will redirect to the public or private page
     url(r'^deletecomment/(?P<comm_id>\d+)$', views.deletecomment), #This is the process for deleting a comment this will redirect to the public or private page
     url(r'^logout$', views.logout), #This is the process for logging out this will redirect to the page where you log out or register
]