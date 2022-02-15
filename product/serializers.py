from rest_framework import serializers

from product.models import Product
from establishment.serializers import EstablishmentSerializer

class ProductSerializer(serializers.ModelSerializer):
    establishment = EstablishmentSerializer()

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'unit_price', 'quantity', 'url_photo',
                  'establishment')
        read_only_fields = ('created_at', 'is_active')
