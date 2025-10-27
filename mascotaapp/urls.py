from django.urls import path
from mascotaapp.views import miform  

urlpatterns = [
    path('miform/', miform, name='miform'),
]
