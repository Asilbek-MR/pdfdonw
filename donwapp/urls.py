from django.urls import path
from .views import index, show, done


urlpatterns = [
    path('', index, name='index'),
    path('show/', show, name='show'),
    path('done/', done, name='done'),
    
]
