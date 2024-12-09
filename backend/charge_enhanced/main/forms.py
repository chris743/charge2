from django import forms
from .models import Commodities

class CommoditiesForm(forms.ModelForm):
    class Meta:
        model = Commodities
        fields = '__all__'  # Include all fields
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'avgCtnPrice': forms.NumberInput(attrs={'class': 'form-control'}),
            'stdCtnCost': forms.NumberInput(attrs={'class': 'form-control'}),
            'pricePerPound': forms.NumberInput(attrs={'class': 'form-control'}),
            'netWeightChile': forms.NumberInput(attrs={'class': 'form-control'}),
            'netWeightDomestic': forms.NumberInput(attrs={'class': 'form-control'}),
            'packingCharge': forms.NumberInput(attrs={'class': 'form-control'}),
            'pallets': forms.NumberInput(attrs={'class': 'form-control'}),
            'profitPerBag': forms.NumberInput(attrs={'class': 'form-control'}),
            'promo': forms.NumberInput(attrs={'class': 'form-control'}),
        }
