from django.db import models

from supervision.models import Timetable
from centres.models import ExamSeries

# Create your models here.

class Committee(models.Model):
    series = models.ForeignKey(ExamSeries, verbose_name="Series", on_delete=models.DO_NOTHING)
    committee_name = models.CharField(max_length=50)
    committee_day = models.CharField(max_length=50)

    class Meta:
        unique_together = ['series',committee_name,'committee_day']
        verbose_name = "committee"
        verbose_name_plural = "committee"

    def __str__(self):
        return f'{self.series} - {self.committee_name} - {self.committee_day}' 

    # def get_absolute_url(self):
    #     return reverse("committee_detail", kwargs={"pk": self.pk})


class Committee(models.Model):
    committe_letter = models.CharField(max_length=50)


class AwardsPapers(models.Model):
    paper = models.OneToOneField(Timetable, verbose_name='Awards Paper', on_delete=models.CASCADE)
    Committee = models.ForeignKey()
    

    class Meta:
        verbose_name = "Awards"
        verbose_name_plural = "Awards"

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("awardspapers_detail", kwargs={"pk": self.pk})
