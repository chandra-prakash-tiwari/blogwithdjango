from cgitb import handler
from . import views
from django.urls import path
from mysite.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('', views.BlogHome, name='home'),
    path('add/', views.CreateBlog),
    path('<slug:slug>/', views.BlogDetails,  name='post_detail'),
    path('edit/<slug:slug>/', views.BlogUpdate),
    path('delete/<slug:slug>/', views.BlogDelete),
    path('get_all_by_user', views.GetAllBlogByUser),
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)