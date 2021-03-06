# Generated by Django 3.1.1 on 2020-09-11 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.CharField(max_length=20)),
                ('Description', models.TextField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('group', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='users.group')),
            ],
        ),
    ]
