from rest_framework import serializers

from .models import Person, Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'name', 'zip_code', 'street', 'city', 'state', 'country', 'number')
        read_only_fields = ('created_at', 'is_active')


class PersonSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Person
        fields = ('id', 'first_name', 'last_name', 'email', 'url_photo', 'address')
        read_only_fields = ('created_at', 'is_active')

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)
        address.save()

        person = Person.objects.create(address=address, **validated_data)

        return person
