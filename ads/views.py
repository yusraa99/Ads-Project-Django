from django.shortcuts import render
from .models import Ads
from django.contrib.auth.decorators import login_required
from .forms import AdsForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.

def ads_all(request):
    all_ads=Ads.objects.all()
    context={'all_ads':all_ads}
    return render(request,'ads/ads.html',context)


@login_required
def user_ads_add(request):

    if request.method=="POST":
        user_id=request.user
        form = AdsForm(request.POST,request.FILES)
        if form.is_valid():
            ads=form.save(commit=False)
            ads.user=user_id
            ads.save()
            return redirect('/ads/')
    else:
        form =AdsForm()
    return render(request,'ads/addingAds.html',{'form':form})
    # return render(request,'ads/addingAds.html')

def ads_details(request,ads_url):
    ads_title=ads_url.replace('-',' ')
    ads=Ads.objects.get(title=ads_title)
    
    # print(ads)
    context={'ads':ads}
    return render(request,'ads/adsDetails.html',context)

@login_required
def ads_edit(request,ads_url):

    ads_title=ads_url.replace('-',' ')
    ads=Ads.objects.get(title=ads_title)

    if request.method=="POST":
        adsform=AdsForm(request.POST,request.FILES,instance=ads)
        # profileform=ProfileForm(request.POST,request.FILES,instance=profile)
        if adsform.is_valid():
            adsform.save()
            return redirect(reverse('accounts:user_ads_all'))

    else:
        adsform=AdsForm(instance=ads)

    return render(request,'ads/editAds.html',{'adsform':adsform, 'ads':ads})


@login_required
def ads_delete(request,ads_url):
    ads_title=ads_url.replace('-',' ')
    ads=Ads.objects.get(title=ads_title)

    ads.delete()
    
    return redirect(reverse('accounts:user_ads_all'))
