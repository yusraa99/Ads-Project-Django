from django.shortcuts import render
from django.contrib.auth import authenticate
from .forms import SignupForm,UserForm,ProfileForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Profile
from django.contrib.auth.decorators import login_required
from ads.models import Ads
from django.contrib.auth.models import User

# Create your views here.
def user_contact_info(request,user_contact):
    user1=User.objects.get(username=user_contact)
    # user_id=User.objects.get(id=user1.id)
    user_info=Profile.objects.get(user=user1)
    # print(user_info)
    context={'user':user1,'user_info':user_info}
    return render(request,'accounts/userContactInfo.html',context)

def signup(request):
    if request.method=="POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')
    else:
        form =SignupForm()
    return render(request,'registration/signup.html',{'form':form})

@login_required
def profile(request):
    
    profile=Profile.objects.get(user=request.user)

    return render(request,'accounts/profile.html',{'profile':profile})


@login_required
def profile_edit(request):
    profile=Profile.objects.get(user=request.user)
    # if profile.is_user==True:
    if request.method=="POST":
        userform=UserForm(request.POST,instance=request.user)
        profileform=ProfileForm(request.POST,request.FILES,instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile=profileform.save(commit=False)
            myprofile.user=request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))

    else:
        userform=UserForm(instance=request.user)
        profileform=ProfileForm(instance=profile)

    return render(request,'accounts/profile_edit.html',{'userform':userform,'profileform':profileform})

@login_required
def user_ads_all(request):
    user1=User.objects.get(username=request.user)
    
    print(user1)
    all_ads=Ads.objects.all()
    context={'all_ads':all_ads, 'user1':user1}
    return render(request,'accounts/user_ads_all.html',context)