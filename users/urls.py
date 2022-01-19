from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.view_profile, name='profile'),
    path('profile/edit/', views.modify_profile, name='modify_profile'),
]
