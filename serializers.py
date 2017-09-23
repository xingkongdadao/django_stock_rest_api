from django.utils.timezone import now
from rest_framework import serializers
from stock.models import Stock


class StockSerializer(serializers.ModelSerializer):
    days_since_created = serializers.SerializerMethodField()

    class Meta:
        model = Stock
        fields = '__all__'

    def get_days_since_created(self, obj):
        return (now() - obj.created).days
