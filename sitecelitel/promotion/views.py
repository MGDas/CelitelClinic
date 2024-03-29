from django.views.generic import ListView
from django.views.generic import DetailView
from promotion.models import Promotion
from django.utils import timezone
from clinic.models import Hospital


class PromotionNowListView(ListView):
    model = Promotion
    template_name = 'promotion/promotion_list_now.html'
    context_object_name = 'promotions'
    queryset = Promotion.pub_objects.filter(data_end__gt=timezone.now())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hospital'] = Hospital.objects.all()[0]
        return context


class PromotionPastListView(ListView):
    model = Promotion
    template_name = 'promotion/promotion_list_past.html'
    context_object_name = 'promotions'
    queryset = Promotion.pub_objects.filter(data_end__lt=timezone.now())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hospital'] = Hospital.objects.all()[0]
        return context


class PromotionDetailView(DetailView):
    model = Promotion
    template_name = 'promotion/promotion_detail.html'
    context_object_name = 'promotion'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hospital'] = Hospital.objects.all()[0]

        promotions = list(Promotion.pub_objects.filter(data_end__gt=timezone.now()))
        try:
            context['next_page'] = promotions[promotions.index(self.object) + 1]
        except:
            context['next_page'] = Promotion.pub_objects.first()
        return context
