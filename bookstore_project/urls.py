from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),     #Django Admin
    
    path('accounts/', include('allauth.urls')), #For auth model
    
    path('', include('pages.urls')),     #Local apps pages
    path('books/', include('books.urls')),  #URL path for books app
]
