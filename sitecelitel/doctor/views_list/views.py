import json
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import DetailView
from doctor.models import Doctor, Specialization
from organization.models import Organization, Department
from django.utils import timezone


class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctor/doctor_list.html'
    context_object_name = "doctors"
    queryset = Doctor.pub_objects.all()
    paginate_by = 16

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['specializations'] = Specialization.objects.all().only('name').order_by('name')
        return context



class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'doctor/doctor_detail.html'
    context_object_name = 'doctor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['videos'] = self.object.videos.filter(public=True)
        # context['articles'] = self.object.articles.filter(public=True)
        # context['reviews'] = self.object.review.filter(public=True)
        # context['other_doctors'] = Doctor.pub_objects.filter(specialization__in=self.object.specialization.all()).exclude(pk=self.object.pk)
        # context['promotions'] = self.object.promotions.filter(public=True).filter(data_end__gt=timezone.now())
        return context


def get_filter_doctors_data(request):

    if request.method == 'GET':
        name = request.GET.get('orderFiltersName', None)
        spec = request.GET.get('orderFiltersSpecialization', None)
        addr = request.GET.get('orderFiltersAddress', None)
        child = request.GET.get('orderFiltersChild', None)

        organ = Organization.objects.filter(address__icontains=addr)
        depart = Department.objects.filter(organization__in=organ)
        specials = Specialization.objects.filter(name__icontains=spec)

        doctors = Doctor.pub_objects.filter(
            full_name__icontains=name,
            specialization__in=specials,
            department__in=depart,
            childish=True if child == 'on' else False
        )

        data = []
        for doctor in doctors:
            response_data = {}
            response_data['name'] = f"{doctor.full_name}"
            response_data['avatar'] = doctor.avatar.url if doctor.avatar else None
            response_data['url'] = f"/doctors/{doctor.pk}"
            response_data['degree'] = doctor.academic_degree
            response_data['experience'] = doctor.experience
            data.append(response_data)

        return HttpResponse(json.dumps(data,  indent=4), content_type='application/json')
