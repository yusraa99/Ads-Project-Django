from django import forms
from .models import Ads


# title
# location
# image
# price 
# description
# category

class AdsForm(forms.ModelForm):
    class Meta:
        model = Ads
        fields = ['title','location','image','price','description','category']