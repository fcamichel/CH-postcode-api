from postcode.models import PLZO
from rest_framework import serializers


class PostCodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PLZO
        fields = ('postcode', 'city_name', 'canton_abbrev', 'lang')
