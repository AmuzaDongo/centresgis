from django import forms
# from django.forms import modelformset_factory, BaseModelFormSet
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout

from .models import PoliceStation, District, Region, Program


class centresForm(forms.Form):
    station = forms.ModelChoiceField(queryset=PoliceStation.objects.all(), required=False, label="Police station")
    district = forms.ModelChoiceField(queryset=District.objects.all(), required=False, label="District")
    region = forms.ModelChoiceField(queryset=Region.objects.all(), required=False, label="Region")
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-centresform'
        self.helper.form_class = 'px-2'
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-inline'
        # self.helper.field_template = 'bootstrap4/layout/inline_field.html'
        # self.helper.layout = Layout('email','password')
        # self.helper.form_action = 'submit_survey'
        self.helper.add_input(Submit('submit', 'View Centres'))

class ProgramsForm(forms.Form):
    program = forms.ModelChoiceField(queryset=Program.objects.all(), required=False, label="Program")


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-ProgramsForm'
        self.helper.form_class = 'px-2'
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-inline'
        # self.helper.field_template = 'bootstrap4/layout/inline_field.html'
        # self.helper.layout = Layout('email','password')
        # self.helper.form_action = 'submit_survey'
        self.helper.add_input(Submit('submit', 'View Centres for Program'))