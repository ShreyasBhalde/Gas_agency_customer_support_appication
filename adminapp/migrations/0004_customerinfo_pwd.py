# Generated by Django 4.2.3 on 2023-08-12 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_alter_servicerequest_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerinfo',
            name='pwd',
            field=models.CharField(default=123, max_length=10),
            preserve_default=False,
        ),
    ]
