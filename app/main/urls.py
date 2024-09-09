from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
    

app_name = 'main'
urlpatterns = [
path(
    "", 
    views.BookHomeView.as_view(),
    name="home-page"
    ),   
    path(
    'login/',
    auth_views.LoginView.as_view(),
    name='login-page'
),
 path(
     'logout/',
     views.LogoutView.as_view(),
     name='logout'
 ),
path(
    'user/create',
    views.CreateUser.as_view(),
    name='create-page'
),
path(
    'user/edit/<uuid:id>',
    views.EditeUserView.as_view(),
    name='edit-user'
),
path(
    'user/profile',
    views.UserProfileView.as_view(),
    name='user-profile'
),


]                                           
