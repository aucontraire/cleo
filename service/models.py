import binascii
import bcrypt
from django.db import models
import os
import phonenumbers
import uuid


def standardize_phone(phone_number):
    """Standardizes phone number to E164 format
       Args:
           phone_number (str): user phone number
       Returns:
           phone_number (str): number in E164 format (e.g., '+14159781111')
    """
    phone_number = phonenumbers.parse(phone_number, "US")
    phone_number_formatted = phonenumbers.format_number(
                phone_number, phonenumbers.PhoneNumberFormat.E164)
    return phone_number_formatted


class Guide(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=60)
    email = models.CharField(unique=True, max_length=60)

    def save(self, *args, **kwargs):
        if self.phone_number:
            self.phone_number = standardize_phone(self.phone_number)
        super().save(*args, **kwargs)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Company(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=128)

    def __str__(self):
        return "{}".format(self.name)


class Family(models.Model):
    FEMALE = 'female'
    MALE = 'male'
    INTERSEX = 'intersex'
    OTHER = 'other'
    GENDER_CHOICES = (
        (FEMALE, 'female'),
        (MALE, 'male'),
        (INTERSEX, 'intersex'),
        (OTHER, 'other'),
    )

    id = models.CharField(primary_key=True, default=uuid.uuid4, max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField(null=True)
    birth_date = models.DateField(null=True)
    baby_gender = models.CharField(blank=True, choices=GENDER_CHOICES, default='', max_length=60)
    main_address = models.CharField(max_length=128)
    company = models.ForeignKey(Company, null=True,on_delete=models.CASCADE)
    guide = models.ForeignKey(Guide, null=True, on_delete=models.CASCADE)


class User(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=60)
    email = models.CharField(unique=True, max_length=60)
    address = models.CharField(max_length=128)
    activation_code = models.CharField(max_length=60)
    password = models.CharField(blank=True, max_length=128)
    family = models.ForeignKey(Family, null=True, on_delete=models.CASCADE)

    def set_password(self, raw_password):
        self.password = bcrypt.hashpw(
            bytes(raw_password, 'utf-8'), bcrypt.gensalt()).decode('utf-8')

    def save(self, *args, **kwargs):
        if not self.activation_code:
            self.activation_code = binascii.hexlify(os.urandom(8)).decode()
        if self.phone_number:
            self.phone_number = standardize_phone(self.phone_number)
        if self.family and len(self.family.user_set.all()) == 2:
            raise AttributeError('Families are limited to two Users')
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
