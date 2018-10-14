from django.db.utils import IntegrityError
from django.test import TestCase
from .models import Company, Family, Guide, User


class UserModelTests(TestCase):

    def test_single_user_creation(self):
        user = User(
            first_name='Paco',
            last_name='Murcia',
            phone_number='415-694-7777',
            email='hello@aol.com',
            address='55 Main St.',
            password=''
        )
        user.save()

        self.assertEqual('Paco Murcia', str(user))
        self.assertEqual('+14156947777', user.phone_number)
        self.assertEqual(16, len(user.activation_code))

    def test_user_email_conflict(self):
        with self.assertRaises(IntegrityError):
            user1 = User(
                first_name='Paco',
                last_name='Murcia',
                phone_number='415-555-7777',
                email='hello@aol.com',
                address='55 Main St.',
                password=''
            )
            user1.save()

            user2 = User(
                first_name='Pepe',
                last_name='Martinez',
                phone_number='415-555-8888',
                email='hello@aol.com',
                address='575 Market St.',
                password=''
            )
            user2.save()

    def test_set_user_password(self):
        user = User(
            first_name='Paco',
            last_name='Murcia',
            phone_number='415-694-7777',
            email='hello@aol.com',
            address='55 Main St.',
            password=''
        )
        user.save()
        user = User.objects.get(pk=user.id)
        raw_password = 'password123'
        user.set_password(raw_password)
        user.save()

        self.assertNotEqual(raw_password, user.password)
        self.assertEqual(60, len(user.password))


class FamilyModelTests(TestCase):

    def test_single_family_creation(self):
        family = Family(
            baby_gender='male',
            main_address='55 Main St.'
        )
        family.save()

        self.assertEqual('male', family.baby_gender)

    def test_single_family_creation_with_guide(self):
        guide = Guide(
            first_name='Lola',
            last_name='Pantoja',
            phone_number='415-694-5555',
            email='hello@aol.com',
        )
        guide.save()

        family = Family(
            baby_gender='female',
            main_address='575 Market St.',
            guide=guide
        )
        family.save()

        self.assertEqual('female', family.baby_gender)
        self.assertEqual('Lola Pantoja', str(family.guide))

    def test_single_family_creation_with_company(self):
        company = Company(
            name='Slack',
            address='1355 Market St.'
        )
        company.save()

        family = Family(
            baby_gender='female',
            main_address='575 Market St.',
            company=company
        )
        family.save()

        self.assertEqual('female', family.baby_gender)
        self.assertEqual('Slack', str(family.company))

    def test_single_family_creation_with_guide_and_company(self):
        guide = Guide(
            first_name='Lola',
            last_name='Pantoja',
            phone_number='415-694-5555',
            email='hello@aol.com',
        )
        guide.save()

        company = Company(
            name='Slack',
            address='1355 Market St.'
        )
        company.save()

        family = Family(
            baby_gender='female',
            main_address='575 Market St.',
            guide=guide,
            company=company
        )
        family.save()

        self.assertEqual('female', family.baby_gender)
        self.assertEqual('Slack', str(family.company))
        self.assertEqual('Lola Pantoja', str(family.guide))


    def test_single_family_creation_with_two_users_members(self):
        guide = Guide(
            first_name='Lola',
            last_name='Pantoja',
            phone_number='415-694-5555',
            email='hello@aol.com',
        )
        guide.save()

        company = Company(
            name='Slack',
            address='1355 Market St.'
        )
        company.save()

        family = Family(
            baby_gender='female',
            main_address='575 Market St.',
            guide=guide,
            company=company
        )
        family.save()

        parent1 = User(
            first_name='Lilly',
            last_name='Stone',
            phone_number='415-694-8888',
            email='lilly@aol.com',
            address='55 Main St.',
            password='',
            family=family
        )
        parent1.save()

        parent2 = User(
            first_name='Stan',
            last_name='Sanchez',
            phone_number='415-694-9999',
            email='stan@aol.com',
            address='55 Main St.',
            password='',
            family=family
        )
        parent2.save()

        self.assertEqual('female', family.baby_gender)
        self.assertEqual('Slack', str(family.company))
        self.assertEqual('Lola Pantoja', str(family.guide))
        self.assertEqual(2, len(family.user_set.all()))

    def test_single_family_creation_enforce_limit_of_two_users(self):
        guide = Guide(
            first_name='Lola',
            last_name='Pantoja',
            phone_number='415-694-5555',
            email='hello@aol.com',
        )
        guide.save()

        company = Company(
            name='Slack',
            address='1355 Market St.'
        )
        company.save()

        family = Family(
            baby_gender='female',
            main_address='575 Market St.',
            guide=guide,
            company=company
        )
        family.save()

        parent1 = User(
            first_name='Lilly',
            last_name='Stone',
            phone_number='415-694-8888',
            email='lilly@aol.com',
            address='55 Main St.',
            password='',
            family=family
        )
        parent1.save()

        parent2 = User(
            first_name='Stan',
            last_name='Sanchez',
            phone_number='415-694-9999',
            email='stan@aol.com',
            address='55 Main St.',
            password='',
            family=family
        )
        parent2.save()

        with self.assertRaises(AttributeError):
            parent3 = User(
                first_name='Paula',
                last_name='Rubio',
                phone_number='415-555-0000',
                email='paula@gmail.com',
                address='55 Main St.',
                password='',
                family=family
            )
            parent3.save()


class GuideModelTests(TestCase):

    def test_single_guide_creation(self):
        guide = Guide(
            first_name='Paco',
            last_name='Murcia',
            phone_number='415-694-5555',
            email='hello@aol.com',
        )
        guide.save()

        self.assertEqual('Paco Murcia', str(guide))

class CompanyModelTests(TestCase):

    def test_single_company_creation(self):
        company = Company(
            name='Slack',
            address='1355 Market St.'
        )
        company.save()

        self.assertEqual('Slack', str(company))
