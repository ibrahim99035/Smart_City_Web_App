from django.contrib import admin
from django.urls import path, include
import debug_toolbar

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hospital/', include('hospital.urls')), 
    path('__debug__/', include(debug_toolbar.urls)),
    path('', include('base.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)