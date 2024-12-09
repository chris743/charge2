from django.contrib import admin
from .models import Commodities
# Register your models here.
@admin.register(Commodities)
class CommoditiesAdmin(admin.ModelAdmin):
    list_display = ('description', 'avgCtnPrice', 'stdCtnCost', 'pricePerPound')  # Customize fields to display
    search_fields = ('description',)