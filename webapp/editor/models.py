from django.db import models


class SimpleModel(models.Model):
    """
    Testing a simple model.
    """

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
