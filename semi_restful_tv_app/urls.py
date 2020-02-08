from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('shows', views.index),
    path('shows/<int:show_id>', views.showDetails),
    path('shows/<int:show_id>/edit', views.editPage),
    path('shows/<int:show_id>/update', views.update),
    path('shows/<int:show_id>/destroy', views.deleteShow),
    path('shows/new', views.addShowPage),
    path('shows/new/create', views.createShow),
] 