from django.views.generic import DetailView

from organization.models import Organization
from organization.models import Department

from doctor.models import Specialization
from doctor.models import Doctor


class OrganDetailView(DetailView):
    template_name = 'organization/organ_detail.html'
    model = Organization
    context_object_name = 'organ'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reg_phone'] = [phone.strip() for phone in self.object.phone_registry.split(',') if phone]

        departments = Department.pub_objects.filter(organization=self.object)
        doctors = Doctor.pub_objects.filter(department__in=departments)
        doctors_spec = set(doctors.values_list('specialization__name', flat=True))
        specialization = Specialization.objects.filter(name__in=doctors_spec).order_by('name')

        context['doctors'] = doctors
        context['specializations'] = specialization

        organization = list(Organization.pub_objects.all())
        try:
            context['next_page'] = organization[organization.index(self.object) + 1]
        except:
            context['next_page'] = Organization.pub_objects.first()

        return context
