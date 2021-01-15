from django.contrib import admin
from django.urls import include, path

app_name ='blog'

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
]