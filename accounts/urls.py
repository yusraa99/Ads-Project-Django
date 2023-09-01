from django.contrib import admin
from django.urls import path,include
from . import views




app_name='accounts'
urlpatterns = [
    path('signup/',views.signup,name='signup'),
    # path('profile/',views.profile,name='profile'),
    # path('profile/edit/',views.profile_edit,name='profile_edit'),
    path("userContact", views.user_contact_info, name="user_contact_info")
    
   

    

]