from django.contrib import admin
from django.conf import settings
from django.urls import include, path

app_name ='blog'

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns