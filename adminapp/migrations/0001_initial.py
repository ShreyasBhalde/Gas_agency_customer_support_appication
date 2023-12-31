# Generated by Django 4.2.3 on 2023-08-12 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=200)),
                ('contact_no', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'Customerinfo',
            },
        ),
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='Pending', max_length=20)),
                ('request_type', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('attachment', models.FileField(blank=True, null=True, upload_to='media/')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.customer')),
            ],
            options={
                'db_table': 'service_request',
            },
        ),
    ]
