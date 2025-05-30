from django.urls import path
from . import views


app_name = 'listings'

urlpatterns = [
    # Ex: listings/
    path('', views.list_redirect, name='list_redirect'),
    # Ex: listings/5
    path('<int:listing_id>', views.detail, name='detail'),
    path('search', views.search_results, name='search_results'),
]
