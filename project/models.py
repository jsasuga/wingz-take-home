from django.db import models
from datetime import datetime


# user (id_user, role, first_name, last_name, email, phone_number)
class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    role = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=25)

    class Meta:
        db_table = "user"

    def __str__(self):
        return "{} - (Role: {}) [Full Name: {} {}]".format(self.id_user, self.role, self.first_name, self.last_name)


# Ride (id_ride, status, id_rider, from, to)
class Ride(models.Model):
    id_ride = models.AutoField(primary_key=True)
    status = models.CharField(max_length=25)
    rider = models.ForeignKey('User', on_delete=models.CASCADE)
    ride_from = models.CharField(max_length=125)
    ride_to = models.CharField(max_length=125)

    class Meta:
        db_table = "ride"

    def __str__(self):
        return "{} - (Rider: {}) [Status: {}]".format(self.id_ride, self.rider.id_user, self.status)


# ride_event (id_ride_event, id_ride, description, created_at)
class RideEvent(models.Model):
    id_ride_event = models.AutoField(primary_key=True)
    ride = models.ForeignKey('Ride', on_delete=models.CASCADE, related_name='ride_events')
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        db_table = "ride_event"

    def __str__(self):
        return "{} - (Ride: {}) [Description: {}]".format(self.id_ride_event, self.ride.id_ride, self.description)
