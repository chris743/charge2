from django.db import models
import uuid

# Create your models here.
class Commodities (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False, max_length=36)
    description = models.CharField(max_length=30, blank=False)
    avgCtnPrice = models.FloatField(null=False, default=0)
    stdCtnCost = models.FloatField(null=False, default=0)
    pricePerPound = models.FloatField(null=False, default=0)
    standardCtnWeight = models.FloatField(null=False, default=0)
    packingCharge = models.FloatField(null=False, default=0)
    profitPerBag = models.FloatField(null=True, default=0)
    promo = models.FloatField(null=False, default=0)

class BagStyles (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False, max_length=36)
    description = models.TextField(null=False, blank=False)

class BagConsumables (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False, max_length=36)
    description = models.CharField(max_length=30, blank=False)
    cost = models.FloatField(null=False, default=0)
    quantity_per_bag = models.IntegerField(null=False, default=1)

class BagMaterials (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False, max_length=36)
    description = models.CharField(max_length=30, blank=False)
    cost_per_unit = models.FloatField(null=False)





