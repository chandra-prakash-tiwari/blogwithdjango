from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.view_profile, name='profile'),
    path('profile/edit/', views.modify_profile, name='modify_profile'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('password_reset/done/', views.password_reset_done, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('change_password/', views.change_password, name='change_password'),
]
