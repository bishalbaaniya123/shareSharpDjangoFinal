from django.db import models


# Create your models here.
class PictureAll(models.Model):
    # Original
    url = models.CharField(max_length=150)
    file = models.ImageField(upload_to='images/gallery/', default="images")
