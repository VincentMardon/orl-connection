# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-29 21:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=40, unique=True, verbose_name="Nom d'utilisateur")),
                ('date_of_birth', models.DateField(verbose_name='Date de naissance')),
                ('first_name', models.CharField(max_length=40, null=True, verbose_name='Prénom')),
                ('last_name', models.CharField(max_length=40, null=True, verbose_name='Nom de famille')),
                ('delivery_adress', models.CharField(max_length=255, null=True, verbose_name='Adresse')),
                ('delivery_adress_complement', models.CharField(max_length=255, null=True, verbose_name="Complément d'adresse")),
                ('delivery_zip_code', models.IntegerField(null=True, verbose_name='Code postal')),
                ('delivery_town', models.CharField(max_length=50, null=True, verbose_name='Ville')),
                ('billing_adress', models.CharField(max_length=255, null=True, verbose_name='Adresse')),
                ('billing_adress_complement', models.CharField(max_length=255, null=True, verbose_name="Complément d'adresse")),
                ('billing_zip_code', models.IntegerField(null=True, verbose_name='Code postal')),
                ('billing_town', models.CharField(max_length=50, null=True, verbose_name='Ville')),
                ('phone_number', models.IntegerField(null=True, verbose_name='Numéro de téléphone')),
                ('tagline', models.CharField(max_length=140, null=True, verbose_name='Signature')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Mise à jour')),
                ('is_active', models.BooleanField(default=True, verbose_name='Actif')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Administrateur')),
            ],
            options={
                'verbose_name': 'Compte utilisateur',
                'verbose_name_plural': 'Comptes utilisateur',
            },
        ),
    ]
