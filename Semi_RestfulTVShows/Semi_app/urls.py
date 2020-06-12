from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('shows', views.shows),
    path('shows/new', views.add_show_page),
    path('add_show', views.create_show),
    path('shows/<int:show_id>', views.view_show),
    path('shows/<int:show_id>/edit', views.edit_page),
    path('edit_show/<int:show_id>', views.update_show),
    path('delete/<int:show_id>', views.delete)

]