# Generated by Django 4.2.3 on 2023-08-13 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminapp', '0004_customerinfo_pwd'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerinfo',
            name='user',
            field=models.OneToOneField(default=123, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
