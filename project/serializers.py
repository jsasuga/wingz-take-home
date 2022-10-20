from rest_framework import serializers
from .models import User, Ride, RideEvent


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id_user', 'role', 'first_name', 'last_name', 'email', 'phone_number']


class RideEventSerializer(serializers.ModelSerializer):
    ride = serializers.PrimaryKeyRelatedField(
        queryset=Ride.objects.all(),
        required=True
    )

    class Meta:
        model = RideEvent
        fields = ['id_ride_event', 'ride', 'description', 'created_at']


class RideSerializer(serializers.ModelSerializer):
    rider = UserSerializer(many=False, read_only=True)
    ride_events = RideEventSerializer(many=True, read_only=True)

    class Meta:
        model = Ride
        fields = ['id_ride', 'status', 'rider', 'ride_from', 'ride_to', 'ride_events']
