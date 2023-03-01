from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'name',
            'phone_number',
            'guest_number',
            'comment',
            'date',
            'time_from',
            'time_to',
            'table_number',
        ]
