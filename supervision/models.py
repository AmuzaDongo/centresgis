from email.policy import default
from enum import unique
from random import choices
from django.db import models

from centres.models import Centres, ExamSeries, Centres
from django.contrib.auth.models import User
# Create your models here.


class Recconoiter(models.Model):
    Recon_profile = models.ForeignKey(User, related_name="reconprofile", on_delete=models.CASCADE)
    series = models.ForeignKey(ExamSeries, related_name="seiriesrecons", on_delete=models.DO_NOTHING)
    centre = models.ForeignKey(Centres, related_name="centresReconoiters", on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ['series','Recon_profile']
        verbose_name = "recconoiter"
        verbose_name_plural = "recconoiters"

    def __str__(self):
        return f"{self.Recon_profile} - {self.series} - {self.centre}"


class session(models.Model):

    session_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "session"
        verbose_name_plural = "sessions"

    def __str__(self):
        return self.session_name

    # def get_absolute_url(self):
    #     return reverse("session_detail", kwargs={"pk": self.pk})


class TimetableCategory(models.Model):

    categories_name = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']
        verbose_name = "categories"
        verbose_name_plural = "categoriess"

    def __str__(self):
        return self.categories_name

    # def get_absolute_url(self):
    #     return reverse("session_detail", kwargs={"pk": self.pk})

class Timetable(models.Model):

    class Period(models.IntegerChoices):
        Moring = 1
        Afternoon = 2
        

    class Phase(models.IntegerChoices):
        One = 1
        Two = 2
        Three = 3
        Four = 4

    examid = models.CharField( max_length=50)
    examcode = models.CharField(max_length=500)
    examname = models.CharField(max_length=500)
    day = models.DateField()
    period = models.ForeignKey(session, related_name="period", on_delete=models.DO_NOTHING)
    exam_phase = models.IntegerField(choices=Phase.choices, default=1)
    category = models.ForeignKey(TimetableCategory, related_name="categorypapers", on_delete=models.CASCADE)
    ispractical = models.BooleanField(default=False)
    grading_notes = models.TextField(default="")
    reccomendations = models.TextField(default="")
    challenges = models.TextField(default="")

    class Meta:
        ordering = ['examid']
        verbose_name = "timetable"
        verbose_name_plural = "timetables"

    def __str__(self):
        return f"{self.examid} - {self.examcode} - {self.examname}"

    # def get_absolute_url(self):
    #     return reverse("timetable_detail", kwargs={"pk": self.pk})



class ExamSession(models.Model):

    centre = models.ForeignKey(Centres, related_name="centresessions", on_delete=models.CASCADE)
    paper = models.ForeignKey(Timetable, related_name="paperssesions", on_delete=models.CASCADE)
    candidates = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "examsession"
        verbose_name_plural = "examsessions"

    def __str__(self):
        return f"{self.centre} - {self.paper}"

    # def get_absolute_url(self):
    #     return reverse("examsession_detail", kwargs={"pk": self.pk})


class MalpracticeTypes(models.Model):

    malpractice = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Malpractice Type"
        verbose_name_plural = "Malpractice Types"

    def __str__(self):
        return self.malpractice

    # def get_absolute_url(self):
    #     return reverse("Malpracti_detail", kwargs={"pk": self.pk})

class ExamMalpractices(models.Model):

    ExamSession = models.ForeignKey(ExamSession, related_name="malpractices", on_delete=models.CASCADE)
    Malpracticetype = models.ForeignKey(MalpracticeTypes, related_name="malpractices", on_delete=models.CASCADE)
    Reg_details = models.TextField(help_text="Regno names Program")
    notes = models.TextField()

    class Meta:
        verbose_name = "Exam Malpractices"
        verbose_name_plural = "Exammal Practices"

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("exammalpractices_detail", kwargs={"pk": self.pk})
