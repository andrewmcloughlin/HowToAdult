
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from app.views import *
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [

    path('', Policy_table, name ='home'),
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('Policy_table/', Policy_table, name ='Policy_table'),
    path('Policy_map/', Policy_map, name ='Policy_map'),
    path('Category_calendar/', Category_calendar, name ='Category_calendar'),
    path('Category_images/', Category_images, name ='Category_images'),
    path('add_Policy/', add_Policy, name = 'add_Policy'),
    path('update_Policy/<int:id>/', update_Policy, name = 'update_Policy'),
    path('delete_Policy/<int:id>/', delete_Policy, name = 'delete_Policy'),
    path('add_Category/', add_Category, name = 'add_Category'),
    path('update_Category/<int:id>/', update_Category, name = 'update_Category'),
    path('delete_Category/<int:id>/', delete_Category, name = 'delete_Category'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)