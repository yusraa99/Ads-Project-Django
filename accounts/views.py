from django.shortcuts import render
from django.contrib.auth import authenticate
from .forms import SignupForm,UserForm,ProfileForm
from django.contrib.auth import login
from django.shortcuts import redirect

# Create your views here.
def user_contact_info(request):
    return render(request,'accounts/userContactInfo.html')

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
