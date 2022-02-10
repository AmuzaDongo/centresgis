from django.contrib import admin

# Register your models here.

from import_export.admin import ImportExportModelAdmin


from .models import Committee,PaperDepartment, AwardsPapers


@admin.register(Committee)
class CommitteeAdmin(ImportExportModelAdmin):    
    # list_display = ('owner','map_color')
    pass


@admin.register(PaperDepartment)
class PaperDepartmentAdmin(ImportExportModelAdmin):    
    # list_display = ('owner','map_color')
    pass


@admin.register(AwardsPapers)
class AwardsPapersAdmin(ImportExportModelAdmin):    
    # list_display = ('owner','map_color')
    pass
