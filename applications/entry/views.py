from django.shortcuts import render

from django.views.generic import(
    ListView,
    DetailView
)

from .models import Entry, Category
from applications.home.models import Home
from .managers import EntryManager

class EntryListView(ListView):
    template_name = "entry/list.html"
    context_object_name = 'entries'
    paginate_by = 6
    
    
    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["home"] = Home.objects.latest('created')
        return context
    

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        category = self.request.GET.get("category", '')
        # Search query
        outcome = Entry.objects.search_entry(kword, category)
        return outcome


class EntryDetailView(DetailView):
    template_name = "entry/detail.html"
    model = Entry
