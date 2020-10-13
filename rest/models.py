from django.db import models

# Create your models here.
class data(models.Model):
    title = models.CharField(max_length=500)
    url = models.URLField(blank=True)
    img_link = models.URLField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title