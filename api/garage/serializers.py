from rest_framework import serializers
from .models import Garage, TimeTable

class GarageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garage
        fields = ['id',
                  'name',
                  'address',
                  'address_number',
                  'country_code',
                  'hourly_rate',
                  'register_date',
                  'opening_time',
                  'closing_time',
                  'currency',
                  'owner']

    def create(self, validated_data):
        return Garage.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.country_code = validated_data.get('country_code', instance.country_code)
        instance.hourly_rate = validated_data.get('hourly_rate', instance.hourly_rate)
        instance.opening_time = validated_data.get('opening_time', instance.opening_time)
        instance.closing_time = validated_data.get('closing_time', instance.closing_time)
        instance.currency = validated_data.get('currency', instance.currency)
        instance.save()
        return instance

class TimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTable
        fields = ['check_in_time', 'check_out_time',
                  'car',
                  'garage', ]

    def create(self, validated_data):
        return TimeTable.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.check_out_time = validated_data.get('check_out_time', instance.check_out_time )
        instance.check_in_time = validated_data.get('check_in_time', instance.check_in_time )
        instance.car = validated_data.get('car', instance.car)
        instance.garage = validated_data.get('garage', instance.garage)
        
        instance.save()
        return instance