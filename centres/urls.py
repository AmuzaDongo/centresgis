from django.urls import path
from .views import Programsview, centresview, stationsview, CentreCreateView, CentreUpdateView, CentresViewSet, RegionViewSet, ProgramCategoryViewSet
from rest_framework import routers


site_header = "UBTEB Centres Admin"
site_title = "UBTEB Centres Portal"
index_title = "Welcome to UBTEB Admin Portal"

router = routers.SimpleRouter()


router.register(r'api/centres', CentresViewSet, basename="centres-api")
router.register(r'api/programcategories', ProgramCategoryViewSet, basename="centres-api")
router.register(r'api/regions', RegionViewSet, basename="centres-api")
    
urlpatterns = [
    path("", centresview, name='home'),
    path("programsview", Programsview, name='programsview'),
    path("stations", stationsview, name='staions-home'),
    path("centre/new", CentreCreateView.as_view(), name='centre_create'),
    path("centre/<int:pk>/edit", CentreUpdateView.as_view(), name='centre_edit'),

    # path("station/<int:pk>/edit", TenancyUpdateView.as_view(), name='tenancy_edit'),

]

urlpatterns += router.urls
