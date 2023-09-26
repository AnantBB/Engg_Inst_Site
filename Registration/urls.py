from django.urls import path
from . import views

app_name = 'Registration'

urlpatterns = [
    path('', views.home, name = 'home' ),
    path('registration', views.insert, name='insert'),
    path('signup', views.person_data_save, name='person_data_save'),
    path('user',views.create_user, name='create_user'),
    path('login',views.login_user, name='login_user'),
    path('help',views.project_help, name='project_help'),
]