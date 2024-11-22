# Generated by Django 5.0.2 on 2024-11-17 10:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_register_set_password_register_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='register',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='register', to=settings.AUTH_USER_MODEL),
        ),
    ]