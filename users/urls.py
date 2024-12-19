from django.urls import path, include

from .views import LoginUser, RegisterUser, logout_user, personalisation, musical_lit, composition, solfeggio

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('personalisation/', personalisation, name='personalisation'),
    path('musical_lit/', musical_lit, name='musical_lit'),
    path('solfeggio/', solfeggio, name='solfeggio'),
    path('composition/', composition, name='composition'),
]

