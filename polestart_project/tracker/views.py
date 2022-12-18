from rest_framework.response import Response
from rest_framework import viewsets
from tracker.models import Vessel
from tracker.serializers import VesselSerializer

class ShipViewSet(viewsets.ViewSet):
    def list(self, request):
        print('start fetching the list')
        vessels = Vessel.objects.all()
        serializer = VesselSerializer(vessels, many=True)
        return Response(serializer.data)
