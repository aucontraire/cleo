from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from service.models import Company, Family, Guide, User


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


class FamilyTests(APITestCase):

    def test_empty_family_list(self):
        url = reverse('family-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Family.objects.count(), len(response.data))

    def test_create_family(self):
        url = reverse('family-list')
        data = {
            'baby_gender': 'female',
            'main_address': '501 Howard Street'
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(1, Family.objects.count())
        self.assertEqual('female', Family.objects.get().baby_gender)

    def test_update_family(self):
        guide = Guide(
            first_name='Stu',
            last_name='Parsons',
            phone_number='415-655-7777',
            email='disco-stu@yahoo.com'
        )
        guide.save()
        guide_id = guide.id

        family = Family(
            baby_gender='female',
            main_address='501 Howard Street',
        )
        family.save()
        family_id = family.id

        data = {
            'main_address': '510 Howard Street',
            'guide': guide_id
        }

        url = reverse('family-detail', kwargs={ 'pk': family_id })
        response = self.client.put(url, data, format='json')
        family = Family.objects.get()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('510 Howard Street', response.data['main_address'])
        self.assertEqual('Stu Parsons', str(family.guide))


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

    def test_activate_user_not_previously_activated_with_valid_data(self):
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
            'activation_code': user.activation_code,
            'password': 'password123'
        }

        url = reverse('user-activate', kwargs={ 'pk': user_id })
        response = self.client.put(url, data, format='json')
        user = User.objects.get()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual('password123', user.password)

    def test_activate_user_with_missing_data(self):
        user = User(
            first_name='Amparo',
            last_name='Mondragon',
            phone_number='415-694-5555',
            email='amondragon@gmail.com',
            address='55 Main St.',
            password=''
        )
        user.save()
        user_id = user.id

        data = { 'activation_code': user.activation_code }

        url = reverse('user-activate', kwargs={ 'pk': user_id })
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
