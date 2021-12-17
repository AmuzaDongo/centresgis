from django.urls import path
from .views import centresview, stationsview, CentreCreateView, CentreUpdateView
    
urlpatterns = [
    path("", centresview, name='home'),
    path("stations", stationsview, name='staions-home'),
    path("centre/new", CentreCreateView.as_view(), name='centre_create'),
    path("centre/<int:pk>/edit", CentreUpdateView.as_view(), name='centre_edit'),

    # path("station/<int:pk>/edit", TenancyUpdateView.as_view(), name='tenancy_edit'),

]
