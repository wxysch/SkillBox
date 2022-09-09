from django.contrib import admin
from django.urls import path, include
from apps.settings.views import index
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = "index"),
    path('', include('apps.users.urls')),
    path('', include('apps.courses.urls')),
    path('', include('apps.settings.urls')),
    path('accounts/', include('allauth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)