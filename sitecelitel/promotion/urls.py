from django.urls import path
from promotion.views import (
    PromotionNowListView,
    PromotionPastListView,
    PromotionDetailView,
)

urlpatterns = [
    path('now/', PromotionNowListView.as_view(), name='promotion_list_now_url'),
    path('past/', PromotionPastListView.as_view(), name='promotion_list_past_url'),
    path('<int:pk>/', PromotionDetailView.as_view(), name='promotion_detail_url'),
]
