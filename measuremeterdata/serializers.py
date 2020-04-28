from .models import Measure, Country, MeasureType, MeasureCategory
from rest_framework import serializers


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['pk', 'name', 'code']

class MeasureCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasureCategory
        fields = ['pk','name']

class MeasureTypeSerializer(serializers.ModelSerializer):
    category = MeasureCategorySerializer()
    class Meta:
        model = MeasureType
        fields = ['pk', 'name', 'category', 'comment']

class MeasureSerializer(serializers.ModelSerializer):
    type = MeasureTypeSerializer()
    country = CountrySerializer()
    class Meta:
        model = Measure
        fields = ['country', 'type', 'start', 'end', 'sources', 'isregional']
