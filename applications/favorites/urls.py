from django.urls import path

from . import views
app_name = "favorites_app"

urlpatterns = [
    path(
        'profile',
        views.UserPageView.as_view(),
        name='profile',        
    ),
    path(
        'add-entry/<pk>/',
        views.AddFavoritesView.as_view(),
        name='add-favorites',        
    ),
    path(
        'delete-favorites/?<pk>/', 
        views.FavoritesDeleteView.as_view(),
        name='delete-favorites',
    ),
]