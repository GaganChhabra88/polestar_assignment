from django.urls import path
from tracker.views import ship_view, position_view

urlpatterns = [
    path('/api/ships', ship_view, name='ships'),
    path('/api/positions/<imo>', position_view, name='positions')
]