# Generated by Django 4.1.7 on 2023-04-07 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'Staff'},
        ),
    ]
