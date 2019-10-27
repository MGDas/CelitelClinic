from django.views.generic import ListView
from django.views.generic import DetailView
from doctor.models import Doctor


class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctor/doctor_list.html'
    context_object_name = "doctors"
    queryset = Doctor.pub_objects.all()


class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'doctor/doctor_detail.html'
    context_object_name = 'doctor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['videos'] = self.object.videos.filter(public=True)
        context['articles'] = self.object.articles.filter(public=True)
        context['other_doctors'] = Doctor.pub_objects.filter(specialization=self.object.specialization).exclude(pk=self.object.pk)
        return context
