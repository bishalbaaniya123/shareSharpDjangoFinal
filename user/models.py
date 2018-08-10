from django.db import models


class PictureAll(models.Model):
    # Original
    url = models.CharField(max_length=150)
    file = models.ImageField(upload_to='images/gallery/', default="images")
    person = models.CharField(max_length=150, default="bishal")
