from rest_framework import status
from rest_framework.test import APITestCase
from service.models import Booking


class AccountTests(APITestCase):
    url = 'http://127.0.0.1:8000/booking/'

    def test_create_account(self):
        data = {
            "name": "Влад",
            "phone_number": "+78005553535",
            "guest_number": 4,
            "comment": "",
            "date": "2023-02-25",
            "time_from": "12:00",
            "time_to": "13:00",
            "table_number": 3
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)
        self.assertEqual(Booking.objects.get().name, 'Влад')

    def test_get_status_code(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
