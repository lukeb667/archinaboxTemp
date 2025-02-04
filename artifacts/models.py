from django.db import models
import datetime

# Create your models here.

class ArtifactModel(models.Model):
    # Longname
    name = models.CharField(max_length=255)
    site = models.CharField(max_length=255)
    lessonPlan = models.CharField(max_length=255)
    date = models.DateField(null=True) # Datefrom 
    shortDescription = models.TextField(null=True)
    longDescription = models.TextField(null=True)
    thumbnail = models.ImageField(null=True, upload_to="static/")
    model = models.FileField(null=True, upload_to="static/",)
    class Meta:
        verbose_name = "Artifact Model"
        verbose_name_plural = "Artifact Models"

    def __str__(self):
        return self.name
    
class Filter(models.Model):
    name = models.CharField(max_length=255)
    options = models.TextField()

    def get_filter_options(self):
        # Return the first 50 characters of the content
        return [option.strip() for option in self.options.split(',')]