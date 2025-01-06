from django.test import TestCase
from Restaurant.models import MenuItem, Booking

class MenuTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(
            title="test menu",
            price=10.99,
            inventory=5
        )
        self.assertEqual(item.title, "test menu")
        self.assertEqual(item.price, 10.99)
        self.assertEqual(item.inventory, 5)

class BookingTest(TestCase):
    def test_get_booking(self):
        booking = Booking.objects.create(
            customer_name="John Doe",
            booking_date="2025-01-01",
            number_of_guests=4
        )
        self.assertEqual(booking.customer_name, "John Doe")
        self.assertEqual(str(booking.booking_date), "2025-01-01")
        self.assertEqual(booking.number_of_guests, 4)
