from django.views.generic import DetailView
from organization.models import Organization


class OrganDetailView(DetailView):
    template_name = 'organization/organ_detail.html'
    model = Organization
    context_object_name = 'organ'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reg_phone'] = [phone.strip() for phone in self.object.phone_registry.split(',') if phone]
        
        organization = list(Organization.pub_objects.all())
        try:
            context['next_page'] = organization[organization.index(self.object) + 1]
        except:
            context['next_page'] = Organization.pub_objects.first()
            
        return context
