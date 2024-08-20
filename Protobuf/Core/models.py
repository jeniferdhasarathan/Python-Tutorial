from django.db import models


class SampleModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    data = models.BinaryField(null=True)  



