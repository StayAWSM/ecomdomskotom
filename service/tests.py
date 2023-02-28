from rest_framework import status
from rest_framework.test import APITestCase
from service.models import Booking
import socket


class TestsBooking(APITestCase):
    url = f'https://{socket.gethostbyname(socket.gethostname())}/booking/'

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

    def test_incorrect_data_format(self):
        data1 = {
            "name": "Максим",
            "phone_number": "+7800555",
            "guest_number": 4,
            "comment": "",
            "date": "2023-02-25",
            "time_from": "12:00",
            "time_to": "13:00",
            "table_number": 3
        }

        data2 = {
            "name": "Максим",
            "phone_number": "+7800555",
            "guest_number": 4,
            "comment": "",
            "date": "2023-02-25",
            "table_number": 3
        }

        # Case 1
        response = self.client.post(self.url, data1, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Booking.objects.count(), 0)  # Not created in the db

        # Case 2
        response = self.client.post(self.url, data2, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Booking.objects.count(), 0)  # Not created in the db

    def test_get_status_code(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
