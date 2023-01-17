from .models import Menu, Bookings
from rest_framework import serializers

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Menu

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Bookings