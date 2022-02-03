from django.db import models

# Create your models here.

class Committee(models.Model):
    committee_name = models.CharField(max_length=50)
    

    class Meta:
        verbose_name = "committee"
        verbose_name_plural = "committee"

    def __str__(self):
        return self.committee_name

    # def get_absolute_url(self):
    #     return reverse("committee_detail", kwargs={"pk": self.pk})
