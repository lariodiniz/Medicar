from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # API URLS
    path('users/', include('access.urls', namespace='users')),
    path('', include('core.urls', namespace='core')),
]
