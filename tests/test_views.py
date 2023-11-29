# Create unit tests for the views.py file in the Restaurant app. You should have at least one test for each view.

from django.test import TestCase
from rest_framework import status
from Restaurant.models import Booking, Menu
from Restaurant.serializers import BookingSerializer, MenuSerializer

# Write a MenuViewTest class that subclasses the TestCase class.
# Use the setup() method to add a few test instances of the Menu model.
# Next, add another test_getall() instance method to retrieve all the Menu objects added for the test purpose.
# The retrieved objects must serialized, so make sure the method runs assertions to check if the serialized data equals the response.
# Do not forget to comment out permiossion classes in the MenuViewSet class in the Restaurant/views.py file.


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Cheese Pizza", price=12.99, inventory=10)
        Menu.objects.create(title="Pepperoni Pizza", price=14.99, inventory=10)
        Menu.objects.create(title="Veggie Pizza", price=12.99, inventory=10)

    def test_getall(self):
        response = self.client.get("/api/menu/")
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        


# Write a BookingViewTest class that subclasses the TestCase class.
# Use the setup() method to add a few test instances of the Booking model.
# Next, add another test_getall() instance method to retrieve all the Booking objects added for the test purpose.
# The retrieved objects must serialized, so make sure the method runs assertions to check if the serialized data equals the response.
# Do not forget to comment out permiossion classes in the BookingViewSet class in the Restaurant/views.py file.


class BookingViewTest(TestCase):
    def setUp(self):
        Booking.objects.create(
            name="John Doe", no_of_guests=2, booking_date="2021-01-01 12:00"
        )
        Booking.objects.create(
            name="Jane Doe", no_of_guests=4, booking_date="2021-01-01 12:00"
        )
        Booking.objects.create(
            name="Jack Doe", no_of_guests=6, booking_date="2021-01-01 12:00"
        )

    def test_getall(self):
        response = self.client.get("/api/booking/")
        booking = Booking.objects.all()
        serializer = BookingSerializer(booking, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
