from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Commodities
from .serializers import CommoditiesSerializer

class CommoditiesViewSet(viewsets.ModelViewSet):
    queryset = Commodities.objects.all()
    serializer_class = CommoditiesSerializer

    # Override the 'destroy' method to handle DELETE requests
    def destroy(self, request, *args, **kwargs):
        try:
            commodity = self.get_object()
            commodity.delete()  # Delete the commodity from the database
            return Response(status=204)  # Return a 204 No Content status if deletion is successful
        except Commodities.DoesNotExist:
            return Response({"detail": "Commodity not found"}, status=404)
