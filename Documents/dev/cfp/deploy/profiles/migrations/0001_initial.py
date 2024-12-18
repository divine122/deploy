# Generated by Django 5.1.3 on 2024-12-03 12:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=7)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=60)),
                ('state', models.CharField(blank=True, max_length=60)),
                ('country', models.CharField(blank=True, max_length=60)),
                ('front_cover', models.ImageField(blank=True, upload_to='document_front_cover')),
                ('back_cover', models.ImageField(blank=True, upload_to='document_back_cover')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]