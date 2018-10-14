# Generated by Django 2.0 on 2018-10-14 07:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=60, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=60, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('due_date', models.DateField(null=True)),
                ('birth_date', models.DateField(null=True)),
                ('baby_gender', models.CharField(blank=True, choices=[('female', 'female'), ('male', 'male'), ('intersex', 'intersex'), ('other', 'other')], default='', max_length=60)),
                ('main_address', models.CharField(max_length=128)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=60, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('phone_number', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=60, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('phone_number', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=60, unique=True)),
                ('address', models.CharField(max_length=128)),
                ('activation_code', models.CharField(max_length=60)),
                ('password', models.CharField(blank=True, max_length=128)),
                ('family', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service.Family')),
            ],
        ),
        migrations.AddField(
            model_name='family',
            name='guide',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service.Guide'),
        ),
    ]
