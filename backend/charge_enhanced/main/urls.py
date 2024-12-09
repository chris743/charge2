# yourapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommoditiesViewSet

router = DefaultRouter()
router.register(r'commodities', CommoditiesViewSet)

urlpatterns = [
    path('', include(router.urls)),  # This will automatically generate routes for CRUD actions
]
