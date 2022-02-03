from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from rest_framework import serializers
from .models import Accreditation, Centres, PoliceStation, Program, ProgramCategory, Region
from .forms import centresForm, ProgramsForm


# Create your views here.
def centresview(request):
    if request.method == "POST":
        form =centresForm(request.POST)
        if form.is_valid():
            station = request.POST['station']
            district = request.POST['district']
            region = request.POST['region']
            program = request.POST['program']
            centresfilters = {'station_id' : station, 'district_id' : district, 'station__region_id' : region}
            incarguments = {}
            for k, v in centresfilters.items():
                if v:
                    incarguments[k] = v
            centresqueryset = Centres.objects.filter(**incarguments).exclude(location__isnull=True)

    else:
        centresqueryset = Centres.objects.exclude(location__isnull=True)
        form = centresForm()
    context = {'form': form,'centreslist':centresqueryset}
    return render(request,"centres/centresmap.html", context)


def Programsview(request):
    if request.method == "POST":
        form =ProgramsForm(request.POST)
        if form.is_valid():
            program_val = request.POST['program']
            Programsfilters = {'Program' : program_val}
            incarguments = {}
            for k, v in Programsfilters.items():
                if v:
                    incarguments[k] = v
            Programsqueryset = Accreditation.objects.filter(**incarguments)

    else:
        Programsqueryset = Centres.objects.exclude(location__isnull=True)
        form = ProgramsForm()
    context = {'form': form,'centreslist':Programsqueryset}
    return render(request,"centres/programsmap.html", context)


class CentresListView(ListView):
    model = Centres


def stationsview(request):
    stationsqeuryset = PoliceStation.objects.all()
    context = {"centreslist":stationsqeuryset}
    return render(request,"centres/stationsmap.html", context)

class CentreCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Centres
    success_message = "Rental Unit Created Successfully"
    fields = ("__all__")

class CentreUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Centres
    success_message = "Rental Unit Updated Successfully"
    fields = ("__all__")




from rest_framework.viewsets import ReadOnlyModelViewSet
from centres.serializers import CentresSerializer, RegionSerializer, ProgramCategorySerializer
from rest_framework.filters import OrderingFilter, SearchFilter

class CentresViewSet(ReadOnlyModelViewSet):
    queryset = Centres.objects.select_related()
    serializer_class = CentresSerializer
    filter_backend = (SearchFilter, OrderingFilter)
    serach_fields = ['centreno', 'centrename', 'station__stnno', 'station__stn_name']


class RegionViewSet(ReadOnlyModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    filter_backend = (SearchFilter, OrderingFilter)
    serach_fields = ['region_name']

class ProgramCategoryViewSet(ReadOnlyModelViewSet):
    queryset = ProgramCategory.objects.all()
    serializer_class = ProgramCategorySerializer
    filter_backend = (SearchFilter, OrderingFilter)
    serach_fields = ['cat_name','dep_name']


class ProgramCategoryViewSet(ReadOnlyModelViewSet):
    queryset = ProgramCategory.objects.all()
    serializer_class = ProgramCategorySerializer
    filter_backend = (SearchFilter, OrderingFilter)
    serach_fields = ['cat_name','dep_name']
