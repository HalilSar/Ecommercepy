from django.shortcuts import render,redirect
from django.contrib.auth.models import User as user

from django.contrib import auth
from django.contrib import messages
from home.models import UserProfile,Setting

# Create your views here.
def index(request):
    
    current_user = request.user  
    profile = UserProfile.objects.get(user_id=current_user.id)
    settings = Setting.objects.get(pk=1)
    context = {
               'settings':settings,
               'profile':profile,

               
               }
    return render(request,'user/user_profile.html',context)
