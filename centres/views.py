from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Centres, PoliceStation
from .forms import centresForm

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