from importlib import resources
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Absentee, ExamMalpractices, ExamSession, MalpracticeTypes, Recconoiter, Timetable, session, TimetableCategory

# Register your models here.
@admin.register(session)
class SessionAdmin(ImportExportModelAdmin):
    # list_display = [field.name for field in session._meta.get_fields()]
    pass

class ExamMalpracticesInline(admin.TabularInline):
    model = ExamMalpractices


class AbsenteeInline(admin.TabularInline):
    model = Absentee


@admin.register(TimetableCategory)
class TimetableCategoryAdmin(ImportExportModelAdmin):
    # list_display= [field.name for field in TimetableCategory._meta.get_fields()]
    pass
    

@admin.register(Timetable)
class TimetableAdmin(ImportExportModelAdmin):
    # list_display = [field.name for field in Timetable._meta.get_fields()]
    list_display = ['examid','examcode','examname','day','period','exam_phase','category','ispractical']
    search_fields = ["examcode", "examname"]
    list_filter = ['day','category','exam_phase','period',]
    

@admin.register(Recconoiter)
class RecconoiterAdmin(ImportExportModelAdmin):
    list_display =  [field.name for field in Recconoiter._meta.get_fields()]

from .resources import ExamsessionAdminResource

@admin.register(ExamSession)
class ExamSessionAdmin(ImportExportModelAdmin):
    # list_display = ['centre','paper','paper__day','paper__period','candidates',]
    list_display = ['centre','paper','candidates',]
    # resource_class = ExamsessionAdminResource

    inlines = [ExamMalpracticesInline, AbsenteeInline]
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.groups.filter(name='Recconoiter').exists():
            user_centre = Recconoiter.objects.get(Recon_profile=request.user)
            print(user_centre)
            queryset= queryset.filter(centre=user_centre.centre)
        return queryset


@admin.register(MalpracticeTypes)
class MalpracticeTypesAdmin(ImportExportModelAdmin):
    pass



