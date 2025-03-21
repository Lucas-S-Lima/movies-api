# Generated by Django 5.1.3 on 2024-11-28 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('gender', models.CharField(max_length=50)),
                ('running_time', models.IntegerField()),
                ('year_released', models.PositiveIntegerField()),
                ('indicative_rating', models.IntegerField(blank=True, null=True)),
                ('nationality', models.CharField(max_length=50)),
                ('cast', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
