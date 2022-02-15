from rest_framework import serializers

from product.models import Product
from person.serializers import AddressSerializer


class EstablishmentSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Product
        fields = ('id', 'name', 'url_photo', 'quantity', 'url_photo'
                  , 'address')
        read_only_fields = ('created_at', 'is_active')
