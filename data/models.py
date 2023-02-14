from django.db import models
import uuid
from django.contrib.postgres.fields import ArrayField

class Product(models.Model):
    uniqueID=models.UUIDField(primary_key=True, default=uuid.uuid4 ,editable=False, unique=True)
    titulo=models.CharField( max_length=50)
    descripcion=models.TextField(max_length=200)
    tags=ArrayField(models.JSONField(), blank=True)
    precio=models.IntegerField()

    @property
    def sale_price(self):
        return "%.2f" %(float(self.precio)*0.8)