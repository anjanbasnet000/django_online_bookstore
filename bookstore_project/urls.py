from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),     #Django Admin
    path('accounts/', include('django.contrib.auth.urls')), #For auth model
    path('', include('pages.urls')),     #Local apps pages
    path('accounts/', include('users.urls'))
]
