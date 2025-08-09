from django.urls import path
from . import views
urlpatterns = [	
    path('', views.index, name= "index"),
    
    path('home/',views.home,name="home"),
    path('show/',views.list,name="show"),
    path('edit/',views.edit,name="edit"),
    path('delete/',views.delete,name="delete"),
    
    
]