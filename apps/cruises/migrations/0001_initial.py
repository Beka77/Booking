# Generated by Django 4.1 on 2022-11-22 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cruises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('poster', models.ImageField(upload_to='', verbose_name='cruiese/')),
                ('place', models.CharField(max_length=100)),
                ('rate', models.CharField(max_length=100)),
                ('price', models.BigIntegerField()),
            ],
            options={
                'verbose_name': 'Круиз',
                'verbose_name_plural': 'Круизы',
            },
        ),
    ]
