from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    github = models.URLField(max_length=200)
    example = models.URLField(max_length=200)
    description = models.TextField()
    tools = models.CharField(max_length=200)
    category = models.CharField(max_length=200)