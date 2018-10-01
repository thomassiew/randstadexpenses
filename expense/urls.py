from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.ExpenseClaims),  
    url(r'list', views.ExpenseList), 
    
   
]

