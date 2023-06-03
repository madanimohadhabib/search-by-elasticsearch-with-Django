# Generated by Django 4.1.7 on 2023-06-03 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('category', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('prix', models.FloatField()),
            ],
        ),
    ]
