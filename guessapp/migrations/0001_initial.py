# Generated by Django 4.1 on 2023-02-11 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('attempts', models.PositiveIntegerField()),
                ('finished_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
