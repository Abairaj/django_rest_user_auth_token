# Generated by Django 4.1.7 on 2023-02-23 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='date_joined',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
