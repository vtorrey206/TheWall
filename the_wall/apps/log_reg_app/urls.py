from django.conf.urls import url
from . import views
from .models import User

                    
urlpatterns = [
     url(r'^$', views.log_reg), # This is the home page for login and Registration this weill be rendering that page
     url(r'^register$', views.register), # this is the proccess for Registering this will redirect to the Profile Page
     url(r'^login$', views.login), # this is the proccess for Logging in this will redirect to the Profile Page
     url(r'^logout$', views.logout), #This is the process for logging out this will redirect to the page where you log out or register
]