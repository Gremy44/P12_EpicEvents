# Generated by Django 4.1.7 on 2023-04-12 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_user_role_alter_user_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('VT', 'Vente'), ('SP', 'Support'), ('GT', 'Gestion')], default='VT', max_length=7),
        ),
    ]
