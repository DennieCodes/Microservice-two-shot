from django.db import models
# from django.urls import reverse

# class LocationVO(models.Model):
#     import_href = models.CharField(max_length=200, unique=True)
#     closet_name = models.CharField(max_length=200)
#     section_number = models.CharField(max_length=200)
#     shelf_number = models.CharField(max_length=200)

#     def get_api_url(self):
#         return reverse("api_location", kwargs={"pk": self.pk})

#     def __str__(self):
#         return f"{self.closet_name} - {self.section_number}/{self.shelf_number}"

#     class Meta:
#         ordering = ("closet_name", "section_number", "shelf_number")


class Hats(models.Model):
    # fabric = models.CharField(max_length=200)
    style = models.CharField(max_length=200, default="CAP")  #!this is style_name
    # color = models.CharField(max_length=200, default= "blue")
    # picture_url = models.URLField(null=True)
    # location = models.ForeignKey(
    #     LocationVO,
    #     related_name="hats",  #!maybe hats?<<< was location
    #     on_delete=models.CASCADE,
    # )

    def __str__(self):
        return self.name

    # def get_api_url(self):
    #     return reverse("api_hats_detail", kwargs={"pk": self.pk})  #!<<?api_hats_detail?
