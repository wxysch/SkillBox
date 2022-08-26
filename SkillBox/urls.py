from django.contrib import admin
from django.urls import path
from apps.settings.views import index
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = "index"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)