from django import views
from django.urls import path, include

from . import views


urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('loginn', views.loginn, name='loginn'),
    path('logout', views.logout_view, name='logout'),
    path('userSignupSession/<str:pkey>', views.userSignupSession, name='userSignupSession'),
    path('signupUser', views.signupUser, name='signupUser'),

    path('homepage/', include('blog.urls') ),
    #blog app
    

]