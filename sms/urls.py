from django.urls import path
from sms import views

urlpatterns = [
       path('dashboard/', views.index, name="index"),
        path('messages/', views.messages, name="messages"),
        path('reports/',views.reports,name='reports')

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
]