from django.urls import path
from .views import index, show, done, feedback


urlpatterns = [
    path('', index, name='index'),
    path('show/', show, name='show'),
    path('done/', done, name='done'),
    path('feedback/', feedback, name='feedback'),
    
]
