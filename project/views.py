import django_filters
from rest_framework import viewsets, permissions

from .models import User, Ride, RideEvent
from .serializers import UserSerializer, RideSerializer, RideEventSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []
    filterset_fields = ['id_user', 'role', 'first_name', 'last_name', 'email', 'phone_number']


class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all().prefetch_related('rider', 'ride_events')
    serializer_class = RideSerializer
    permission_classes = [permissions.IsAdminUser]
    filterset_fields = ['status', 'rider__first_name', 'rider__last_name', 'rider__email', 'rider__phone_number']


class RideEventViewSet(viewsets.ModelViewSet):
    queryset = RideEvent.objects.all()
    serializer_class = RideEventSerializer
    permission_classes = []
    filterset_fields = ['id_ride_event', 'description', 'created_at']
