# Generated by Django 4.2.5 on 2023-09-15 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iin', models.CharField(max_length=12, unique=True, verbose_name='IIN')),
            ],
        ),
    ]
