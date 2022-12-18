from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from tracker.views import ShipViewSet #, position_view


router = DefaultRouter()

router.register('ships', ShipViewSet, basename='ships'),


urlpatterns = [
    path('', include(router.urls)),
    # router.register('ships', ShipViewSet, basename='ships')
    # path('/api/positions/<imo>', position_view, name='positions')
]