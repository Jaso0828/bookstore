from django.views.generic import ListView
from ..models.publishers import Publisher

class PublisherListView(ListView):
    model = Publisher
    template_name = "publisher_list"  # ili gdje je tvoj template

