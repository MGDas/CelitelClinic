from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

def error_404(request, exception):
    return render(request, '404.html', {})
