import datetime
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView,
    CreateView
)

# Model Entry
from applications.entry.models import Entry

# Model Home
from .models import Home

# Forms
from .forms import SubscribersForm, ContactForm

class HomePageView(TemplateView):
    template_name = "home/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # Load home
        context["home"] = Home.objects.latest('created')
        # Cover page text
        context["coverpage"] = Entry.objects.entry_in_coverpage()
        # Context for articles in home
        context["entry_home"] = Entry.objects.entry_in_home()
        # Entry recents
        context["entry_recents"] = Entry.objects.entry_recents()       
        # Send subscription form 
        context["form"] = SubscribersForm
        return context


class SubscribersCreateView(CreateView):
    form_class = SubscribersForm
    success_url = '.'
    
class ContactCreateView(CreateView):
    form_class = ContactForm
    success_url = '.'

    