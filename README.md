Please utilize the Django REST Framework to design a ride list API that meets these requirements:
1. ✔️ Uses Viewset
2. ✔️ Returns a list of rides in JSON format
3. ✔️ Every ride object in the response has the rider info, and a list of ride events
4. ✔️ Be able to accept parameters to filter by ride statuses, e.g. return all rides in ‘en-route’ status
5. ✔ ️Be able to accept parameters to filter by rider’s email, first/last name, and phone number
6. ✔️ Supports pagination
7. ✔ Only user role ‘admin’ can access this API

Tables:
1. Ride (id_ride, status, id_rider, from, to), user (id_user, role, first_name, last_name, email, phone_number), ride_event (id_ride_event, id_ride, description, created_at)
2. Ride has a foreign key ‘id_user’ which points to the user table
3. Ride_event has a foreign key ‘id_ride’ which points to the ride table


Be sure to follow the RESTful API design principles.

https://www.django-rest-framework.org/




