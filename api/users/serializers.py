from rest_framework import serializers
from .models import Car, CustomerUser

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['license_plate_number', 'license_country_code',
                  'owner',
                  'date_added', ]

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.license_plate_number = validated_data.get('license_plate_number', instance.license_plate_number)
        instance.license_country_code = validated_data.get('license_country_code', instance.license_country_code)
        instance.save()
        return instance

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = ['iban', 'address',
                  'house_number',
                  'zip_code',
                  'is_garage_owner',
                  'user', ]

    def create(self, validated_data):
        return CustomerUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.iban = validated_data.get('iban', instance.iban)
        instance.address = validated_data.get('address', instance.address)
        instance.house_number = validated_data.get('house_number', instance.house_number)
        instance.zip_code = validated_data.get('zip_code', instance.zip_code)
        instance.is_garage_owner = validated_data.get('is_garage_owner', instance.is_garage_owner)
        instance.save()
        return instance