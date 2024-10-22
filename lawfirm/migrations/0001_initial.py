# Generated by Django 5.1.2 on 2024-10-21 23:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('social_reason', models.CharField(max_length=100)),
                ('social_name', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=14)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lawfirm.account')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.address')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CompanyContacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('main', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lawfirm.company')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.email')),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.phone')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LawFirmOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('juridical_person_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lawfirms', to='lawfirm.company')),
                ('physical_person_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lawfirms', to='lawfirm.account')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LawFirm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lawfirm.lawfirmowner')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
