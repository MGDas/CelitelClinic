from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import handler404
from django.conf import settings

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # redactor text django-summernote
    path('summernote/', include('django_summernote.urls')),
    path('', include('clinic.urls')),
]

handler404 = 'clinic.views.error_404'


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]