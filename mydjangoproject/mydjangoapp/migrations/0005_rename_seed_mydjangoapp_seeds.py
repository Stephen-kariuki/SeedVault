# Generated by Django 4.1.13 on 2024-07-19 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mydjangoapp', '0004_seed_delete_seeds'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Seed',
            new_name='mydjangoapp_seeds',
        ),
    ]
