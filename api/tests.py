from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from service.models import Company, Guide, User


class CompanyTests(APITestCase):

    def test_empty_company_list(self):
        url = reverse('company-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Company.objects.count(), len(response.data))

    def test_create_company(self):
        url = reverse('company-list')
        data = {
            'name': 'Slack',
            'address': '500 Howard Street'
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(1, Company.objects.count())
        self.assertEqual('Slack', str(Company.objects.get()))


class GuideTests(APITestCase):

    def test_empty_guide_list(self):
        url = reverse('guide-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Guide.objects.count(), len(response.data))

    def test_create_guide(self):
        url = reverse('guide-list')
        data = {
            'first_name': 'Stu',
            'last_name': 'Parsons',
            'phone_number': '415-655-7777',
            'email': 'disco-stu@yahoo.com'
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(1, Guide.objects.count())
        self.assertEqual('Stu Parsons', str(Guide.objects.get()))


class UserTests(APITestCase):

    def test_empty_user_list(self):
        url = reverse('user-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), len(response.data))

    def test_populated_user_list(self):
        user1 = User(
            first_name='Paula',
            last_name='Rubio',
            phone_number='415-694-8888',
            email='paula@gmail.com',
            address='55 Main St.',
            password=''
        )
        user1.save()

        user2 = User(
            first_name='Paco',
            last_name='Murcia',
            phone_number='415-694-7777',
            email='hello@aol.com',
            address='55 Main St.',
            password=''
        )
        user2.save()

        url = reverse('user-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), len(response.data))

    def test_create_user(self):
        url = reverse('user-list')
        data = {
            'first_name': 'Paco',
            'last_name': 'Murcia',
            'phone_number': '415-694-7777',
            'email': 'hello@aol.com',
            'address': '55 Main St.',
            'password': ''
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(1, User.objects.count())
        self.assertEqual('Paco Murcia', str(User.objects.get()))

    def test_duplicate_user_email_error(self):
        user1 = User(
            first_name='Paula',
            last_name='Rubio',
            phone_number='415-694-8888',
            email='hello@aol.com',
            address='55 Main St.',
            password=''
        )
        user1.save()

        url = reverse('user-list')
        data = {
            'first_name': 'Paco',
            'last_name': 'Murcia',
            'phone_number': '415-694-7777',
            'email': 'hello@aol.com',
            'address': '55 Main St.',
            'password': ''
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_user(self):
        user = User(
            first_name='Paco',
            last_name='Murcia',
            phone_number='415-694-7777',
            email='hello@aol.com',
            address='55 Main St.',
            password=''
        )
        user.save()
        user_id = user.id

        url = reverse('user-detail', kwargs={ 'pk': user_id })
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('Paco', response.data['first_name'])

    def test_update_user(self):
        user = User(
            first_name='Paco',
            last_name='Murcia',
            phone_number='415-694-7777',
            email='hello@aol.com',
            address='55 Main St.',
            password=''
        )
        user.save()
        user_id = user.id

        data = {
            'email': 'paco@gmail.com',
        }

        url = reverse('user-detail', kwargs={ 'pk': user_id })
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('paco@gmail.com', response.data['email'])


    # TODO: add activate user
