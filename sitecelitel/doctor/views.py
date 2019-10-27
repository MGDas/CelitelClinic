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
