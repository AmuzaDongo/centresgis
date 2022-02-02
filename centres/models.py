from curses.ascii import isblank
from django.db import models
from django.contrib.gis.db import models
from django.urls import reverse


import datetime
# Create your models here.

class Region(models.Model):
    region_name = models.CharField(max_length=50)
    region_area = models.PolygonField(srid=4326, null=True, blank=True)

    def __str__(self):
        return f"{self.region_name}"
        
class Bank(models.Model):
    bank_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.bank_name}"

    class Meta:
        ordering = ['id']


class person(models.Model):

    fullname = models.CharField(max_length=200)
    phoneno1 = models.CharField(max_length=12,null=True, blank=True, unique=True)
    phoneno2 = models.CharField(max_length=12,null=True, blank=True, unique=True)
    Phoneno3 = models.CharField(max_length=12,null=True, blank=True, unique=True)
    bank = models.ForeignKey(Bank, null=True, blank=True, on_delete=models.DO_NOTHING)
    bank_branch = models.CharField(max_length=200, null=True , blank=True)
    min_no = models.CharField(max_length=50,null=True, blank=True, unique=True)
    email = models.EmailField(max_length=254,null=True, blank=True, unique=True)
    notes = models.CharField(max_length=500, default="",null=True, blank=True)

    class Meta:
        verbose_name = "person"
        verbose_name_plural = "persons"

    def __str__(self):
        return "{self.fullname} - {self.phoneno1}" 
        # //todo make returned phone no if available

    def get_absolute_url(self):
        return reverse("person_detail", kwargs={"pk": self.pk})


class District(models.Model):
    district_name = models.CharField(max_length=100, null=True, blank=True)
    distric_area = models.PolygonField(srid=4326, blank=True, null=True)
    district_notes = models.TextField(default="")
    district_centre = models.PointField(srid=4326, blank=True, null=True)


    def __str__(self):
        return f"{self.district_name}"

class PoliceStation(models.Model):
    stnno = models.CharField(max_length=10, unique=True)
    stn_name = models.CharField(max_length=100)
    location = models.PointField(srid=4326, blank=True, null=True)
    station_cordinator = models.ForeignKey(to=person, related_name="cordinator", null=True, blank=True,  on_delete=models.SET_NULL)
    station_notes = models.CharField(max_length=100, null=True,blank=True)
    station_address = models.TextField(default="")

    def __str__(self):
        return f"{self.stnno} - {self.stn_name}"

    class Meta:
        ordering = ['stnno']
        verbose_name = 'Station'
        verbose_name_plural = 'Stations'

class Centres(models.Model):
    class Ownership(models.IntegerChoices):
        DORMANT = 0
        GOVERNMENT = 1
        PRIVATE = 2
        OTHER =3
        
    class AccreditationStatus(models.IntegerChoices):
        DORMANT = 0
        PROVISIONAL = 1
        FULL =2

    centreno = models.CharField(max_length=10, unique=True)
    centrename = models.CharField(max_length=500)
    location = models.PointField(srid=4326, blank=True, null=True)
    station = models.ForeignKey(PoliceStation, on_delete=models.DO_NOTHING, null=True, blank=True)
    owner = models.IntegerField(choices=Ownership.choices, default=1)
    centre_head = models.ForeignKey(to=person,related_name="princpal", on_delete=models.DO_NOTHING, null=True, blank=True)
    centre_registrar = models.ForeignKey(to=person, related_name="registrar", on_delete=models.DO_NOTHING , null=True, blank=True)
    accreditation_staus = models.IntegerField(choices=AccreditationStatus.choices, default=1)
    accreditation_expiry = models.DateField(default=datetime.date(2022,6,15))
    tr_centre = models.PositiveIntegerField(default=50000)
    tr_kla = models.PositiveIntegerField(default=100000)
    verified = models.BooleanField(default=False)

    
    def __str__(self):
        return f"{self.centreno} - {self.centrename}"

    class Meta:
        ordering = ['centreno']
        verbose_name_plural = 'centres'


class Department(models.Model):
    dep_name = models.CharField(max_length=50)
    dep_head = models.ForeignKey(person, on_delete=models.DO_NOTHING, blank=True, null=True)
    
    def __str__(self):
        return f"{self.dep_name} - {self.dep_head}"

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = 'Departments'

class ProgramCategory(models.Model):

    cat_name  = models.CharField(max_length=50)
    dep_name = models.ForeignKey(Department,on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        verbose_name = "ProgramCategory"
        verbose_name_plural = "ProgramCategories"

    def __str__(self):
        return f"{self.cat_name} - {self.dep_name}"

    
class Program(models.Model):
    prg_code = models.CharField(max_length=20, unique= True)
    prg_name = models.CharField(max_length=200)
    prg_category = models.ForeignKey(ProgramCategory, on_delete=models.DO_NOTHING, null=True, blank=True)
    
    class Meta:
        verbose_name = "Program"
        verbose_name_plural = "Programs"

    def __str__(self):
        return f"{self.prg_code} - {self.prg_name}"


class ExamSeries(models.Model):
    series_name = models.CharField(max_length=50)

    class Meta:
            ordering = ['id']
            verbose_name = "ExamSeries"
            verbose_name_plural = "ExamSeries"
    
    def __str__(self):
        return self.series_name


class Accreditation(models.Model):
    centreno = models.ForeignKey(Centres, related_name="centreprograms", on_delete=models.DO_NOTHING, null=True, blank=True)
    Program = models.ForeignKey(Program, related_name="programcentres", on_delete= models.DO_NOTHING, null=True, blank=True)
    expiry = models.DateField(default=datetime.date(2022,6,15))

    class Meta:
        unique_together = ("centreno","Program")
        verbose_name = "Accreditation"
        verbose_name_plural = "Accreditations"
    
    def __str__(self):
        return f"{self.centreno} - {self.Program}"

    