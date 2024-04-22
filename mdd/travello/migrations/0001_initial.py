# Generated by Django 4.2.1 on 2024-04-22 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('img', models.ImageField(upload_to='pics')),
                ('days', models.CharField(max_length=25)),
                ('rating', models.TextField()),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]
