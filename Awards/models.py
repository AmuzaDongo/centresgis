from django.db import models

# Create your models here.

class Committee(models.Model):

    

    class Meta:
        verbose_name = "committee"
        verbose_name_plural = "committees"

    def __str__(self):
        return self.committeename

    # def get_absolute_url(self):
    #     return reverse("committee_detail", kwargs={"pk": self.pk})
