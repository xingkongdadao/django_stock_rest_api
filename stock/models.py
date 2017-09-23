from uuid import uuid1

from django.db import models


# Create your models here.


class Stock(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid1, editable=False)
    name = models.TextField()
    price = models.FloatField()
    rating = models.FloatField()
    desc = models.TextField()
    categories = models.TextField()
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "stock"
