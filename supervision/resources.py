from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget

from .models import Timetable, ExamSession
from centres.models import Centres

# class ExamsessionAdminResource(resources.ModelResource):
#     centre = fields.Field(column_name='centreno', attribute='centreno', widget=ForeignKeyWidget(Centres,field='centreno'))
#     examid = fields.Field(column_name='Examid', attribute='examid', widget=ForeignKeyWidget(Timetable,field='examid'))

#     class Meta:
#         model = ExamSession
#         fields = ('id','centre','examid','candidates')

class ExamsessionAdminResource(resources.ModelResource):
    centre = fields.Field(column_name='centreno', attribute='centreno', widget=ForeignKeyWidget(Centres,field='centreno'))
    examid = fields.Field(column_name='Examid', attribute='examid', widget=ForeignKeyWidget(Timetable,field='examid'))

    class Meta:
        model = ExamSession
        fields = ('id','centre__centreno','paper__examid','candidates')
        export_order = ('id','centre__centreno','paper__examid','candidates')
# //TODO Fix import of sessions