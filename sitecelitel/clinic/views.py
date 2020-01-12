from django.shortcuts import render
from django.views.generic import TemplateView

from doctor.models import Review
from doctor.models import Video
from doctor.models import Consultation

from clinic.models import Slider
from clinic.models import Partner


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['reviews'] = Review.objects.all()[:6]
        context['videos'] = Video.objects.all()[:4]
        context['consultations'] = Consultation.objects.all()[:6]
        context['sliders'] = Slider.pub_objects.all()
        context['partners'] = Partner.pub_objects.all()
        return context


def error_404(request, exception):
    return render(request, '404.html', {})
