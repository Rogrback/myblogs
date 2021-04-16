from django.shortcuts import render
#
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
#
from django.views.generic import (
    View,
    ListView,
    DeleteView
)

#
from .models import Favorites
from applications.entry.models import Entry
from applications.home.models import Home

class UserPageView(ListView):
    template_name = "favorites/profile.html"
    context_object_name = "entries_user"
    login_url = reverse_lazy('users_app:user-login')

    def get_context_data(self, **kwargs):
        context = super(UserPageView, self).get_context_data(**kwargs)
        context["home"] = Home.objects.latest('created')
        return context

    def get_queryset(self):
        return Favorites.objects.entries_user(self.request.user)

class AddFavoritesView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users_app:user-login')

    def post(self, request, *args, **kwargs):
        # Recover the user
        usuario = self.request.user
        entrada = Entry.objects.get(id=self.kwargs['pk'])
        # Register favorite
        Favorites.objects.create(
            user=usuario,
            entry=entrada,
        )

        return HttpResponseRedirect(
            reverse(
                'favorites_app:profile',
            )
        )

class FavoritesDeleteView(DeleteView):
    model = Favorites
    success_url = reverse_lazy('favorites_app:profile')