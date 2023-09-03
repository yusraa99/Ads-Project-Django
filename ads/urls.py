from django.contrib import admin
from django.urls import path,include
from . import views

app_name='ads'
urlpatterns = [
    path('',views.ads_all,name='all_ads'),
    path('<str:ads_url>',views.ads_details,name='ads_details'),
    path('edit/<str:ads_url>',views.ads_edit,name='ads_edit'),
    path('delete/<str:ads_url>',views.ads_delete,name='ads_delete'),
    path('add/',views.user_ads_add,name='user_ads_add'),
    
]
