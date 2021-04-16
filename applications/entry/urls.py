from django.urls import path

from . import views
app_name = "entry_app"

urlpatterns = [
    path(
        'entries/',
        views.EntryListView.as_view(),
        name='entry-list',        
    ),
    path(
        'entry/<slug>/',
        views.EntryDetailView.as_view(),
        name='entry-detail',        
    ),
]