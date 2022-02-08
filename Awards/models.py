from django.db import models

from supervision.models import Timetable
from centres.models import ExamSeries

# Create your models here.

class Committee(models.Model):
    series = models.ForeignKey(ExamSeries, verbose_name="Series", on_delete=models.DO_NOTHING)
    committee_name = models.CharField(max_length=50)
    committee_day = models.CharField(max_length=50)

    class Meta:
        unique_together = ['series','committee_name','committee_day']
        verbose_name = "committee"
        verbose_name_plural = "committee"

    def __str__(self):
        return f'{self.series} - {self.committee_name} - {self.committee_day}' 

    # def get_absolute_url(self):
    #     return reverse("committee_detail", kwargs={"pk": self.pk})

class PaperDepartment(models.Model):
    paper_dept = models.CharField(max_length=50)    

    class Meta:
        verbose_name = "PaperDepartment"
        verbose_name_plural = "PaperDepartment"

    def __str__(self):
        return self.paper_dept
    
     # def get_absolute_url(self):
    #     return reverse("Paperfields_detail", kwargs={"pk": self.pk})

class AwardsPapers(models.Model):
    paper = models.OneToOneField(Timetable, verbose_name='Awards Paper', on_delete=models.CASCADE)
    committee = models.ForeignKey(to=Committee,related_name='comm_papers', on_delete=models.DO_NOTHING)
    committe_trade = models.ManyToManyField(to=PaperDepartment,related_name='trades')
    

    class Meta:
        verbose_name = "Awards"
        verbose_name_plural = "Awards"

    def __str__(self):
        return f'{self.name} - {self.committee}'

    # def get_absolute_url(self):
    #     return reverse("awardspapers_detail", kwargs={"pk": self.pk})
