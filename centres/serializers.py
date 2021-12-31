from django.db.models import fields
from rest_framework import serializers

from centres.models import Centres, Program, Accreditation, PoliceStation, ProgramCategory, Region


class PoliceStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliceStation
        fields = '__all__'


class AccreditationSerializer(serializers.ModelSerializer):
    prg_code = serializers.CharField(source='Program.prg_code')
    prg_name = serializers.CharField(source='Program.prg_name')
    class Meta:
        model = Accreditation
        # fields = '__all__'
        fields = ['centreno','Program','prg_code','prg_name']



class CentresSerializer(serializers.ModelSerializer):
    station = PoliceStationSerializer()
    centreprograms = AccreditationSerializer(many=True, read_only=True)
    class Meta:
        model = Centres
        fields = '__all__'
    

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class ProgramCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramCategory
        fields = '__all__'

