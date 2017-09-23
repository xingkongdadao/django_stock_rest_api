# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from serializers import StockSerializer
from stock.models import Stock


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = (IsAuthenticated,)
