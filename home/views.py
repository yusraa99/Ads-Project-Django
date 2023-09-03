from django.shortcuts import render
from ads.models import Ads
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.
def index(request):
    all_ads=Ads.objects.all()[:3]
    context={'all_ads':all_ads}
    return render(request,'home/home.html', context)
