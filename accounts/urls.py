from django.contrib import admin
from django.urls import path,include
from . import views




app_name='accounts'
urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('profile/edit/',views.profile_edit,name='profile_edit'),
    path('profile/my-ads/',views.user_ads_all,name='user_ads_all'),
    path("userContact/<str:user_contact>", views.user_contact_info, name="user_contact_info")
    
   

    

]