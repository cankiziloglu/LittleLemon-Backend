from django.test import TestCase
from Restaurant.models import Booking, Menu


class MenuTest(TestCase):
    def test_create_item(self):
        item = Menu.objects.create(title="Cheese Pizza", price=12.99, inventory=10)
        self.assertEqual(item.title, "Cheese Pizza")


class BookingTest(TestCase):
    def test_create_booking(self):
        booking = Booking.objects.create(
            name="John Doe", no_of_guests=2, booking_date="2021-01-01 12:00"
        )
        self.assertEqual(booking.name, "John Doe")
        self.assertEqual(booking.no_of_guests, 2)
        self.assertEqual(booking.booking_date, "2021-01-01 12:00")
