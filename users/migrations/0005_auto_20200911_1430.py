# Generated by Django 3.1.1 on 2020-09-11 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200911_0950'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='Description',
            new_name='description',
        ),
    ]
