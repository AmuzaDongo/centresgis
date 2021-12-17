from django.db import models
from django.db.models.base import Model
from leaflet.admin import LeafletGeoAdmin, LeafletGeoAdminMixin
from django.urls import reverse
from django.contrib import admin
from .models import Region, PoliceStation, Centres, District
from import_export.admin import ImportExportModelAdmin
from django.utils.http import urlencode
from django.utils.html import format_html



# @admin.register(Centres)
# class CentresAdmin(ImportExportModelAdmin):
    
#     list_display = ("centreno", "centrename", "station","view_Programs_link","location","district","owner","centre_head","centre_registrar","accreditation_staus","accreditation_expiry")
#     # list_filter = ("prg_code","prg_category" )
#     # search_fields = ("prgcode__startswith", )

#     def view_Programs_link(self, obj):
#         count = obj.accreditation_set.count()
#         url = (
#             reverse("admin:registration_accreditation_changelist")
#             + "?"
#             + urlencode({"centreno__id": f"{obj.id}"})
#         )
#         return format_html('<a href="{}">{} Programs</a>', url, count)

#     view_Programs_link.short_description = "Programs"



class LocationFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'Has Location'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'location'

    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Has Location'),
            ('No', 'No Location'),
        )

    def queryset(self, request, queryset):
        if self.value() == "Yes":
            return queryset.exclude(location__isnull=True)
        if self.value() == "No":
            return queryset.filter(location__isnull=True)


@admin.register(Centres)
class CentresAdmin(LeafletGeoAdmin, ImportExportModelAdmin):
    list_display = ("centreno", "centrename","centre_head", "location", "station","owner","accreditation_staus")
    search_fields = ['centreno','centrename']
    list_filter = [LocationFilter,'owner','accreditation_staus','accreditation_staus',"station"]
    # list_editable = ['owner','accreditation_staus','location']

@admin.register(PoliceStation)
class PoliceStationAdmin(LeafletGeoAdmin, ImportExportModelAdmin):
    list_display = ("stnno", "stn_name","location", "station_cordinator")
    search_fields = ["stnno", "stn_name"]
    # list_filter = ['owner','accreditation_staus']

@admin.register(District)
class DistrictAdmin(LeafletGeoAdmin,ImportExportModelAdmin):
    pass

@admin.register(Region)
class RegionAdmin(LeafletGeoAdminMixin,ImportExportModelAdmin):
    pass

