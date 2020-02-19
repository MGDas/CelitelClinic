from django.urls import path, include
from clinic.views import IndexView, HospitalView, MedicalCertificatesView


urlpatterns = [
    path('', IndexView.as_view(), name='index_url'),
    path('hospital/', HospitalView.as_view(), name='hospital_url'),
    path('certificates/', MedicalCertificatesView.as_view(), name='certificates_url'),
    path('articles/', include('article.urls')),
    path('tags/', include('tag.urls')),
    path('doctors/', include('doctor.urls')),
    path('news/', include('new.urls')),
    path('promotions/', include('promotion.urls')),
    path('russian_doctors/', include('rusdoc.urls')),
    path('faq/', include('faq.urls')),
    path('vacancy/', include('vacancy.urls')),
    path('service/', include('service.urls')),
    path('organization/', include('organization.urls'))
]
