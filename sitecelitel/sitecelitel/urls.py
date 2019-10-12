from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # redactor text django-summernote
    path('summernote/', include('django_summernote.urls')),
    path('', include('clinic.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
