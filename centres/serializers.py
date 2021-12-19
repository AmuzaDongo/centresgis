from django.db.models import fields
from rest_framework import serializers

from centres.models import Centres, Program, Accreditation, PoliceStation


class PoliceStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliceStation
        fields = '__all__'


class CentresSerializer(serializers.ModelSerializer):
    station = PoliceStationSerializer()
    
    class Meta:
        model = Centres
        fields = '__all__'
        


class AccreditationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accreditation
        fields = '__all__'


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'

