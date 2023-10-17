from django.db import models
from django.urls import reverse

class BinVO(models.Model):
  import_href = models.CharField(max_length=200, unique=True)
  closet_name = models.CharField(max_length=200)

  def __str__(self):
    return self.closet_name

class Shoe(models.Model):
  model_name = models.CharField(max_length=200)
  manufacturer_name = models.CharField(max_length=200)
  color = models.CharField(max_length=100)
  picture_url = models.URLField(max_length=200)
  assigned_bin = models.ForeignKey(
    BinVO,
    related_name="shoes",
    on_delete=models.CASCADE
  )

  def __str__(self):
    return self.name

  def get_api_url(self):
    return reverse("api_list_shoes", kwargs={"pk": self.pk})
