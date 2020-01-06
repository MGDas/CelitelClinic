from django.urls import path
from faq.views import FaqViewList

urlpatterns = [
    path('', FaqViewList.as_view(), name='faq_list_url')
]
