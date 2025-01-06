from django.test import TestCase
from django.urls import reverse
from Restaurant.models import MenuItem, Booking

class MenuListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_menus = 5
        for menu_id in range(number_of_menus):
            MenuItem.objects.create(
                title=f'Test Menu {menu_id}',
                price=10.99 + menu_id,
                inventory=5
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('menu_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('menu_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu_list.html')

    def test_pagination_is_five(self):
        response = self.client.get(reverse('menu_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertEqual(len(response.context['menu_list']), 5)

class BookingListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_bookings = 5
        for booking_id in range(number_of_bookings):
            Booking.objects.create(
                customer_name=f'John Doe {booking_id}',
                booking_date=f'2025-01-0{booking_id+1}',
                number_of_guests=4
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/booking/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('booking_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('booking_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking_list.html')

    def test_pagination_is_five(self):
        response = self.client.get(reverse('booking_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertEqual(len(response.context['booking_list']), 5)
