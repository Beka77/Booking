# Generated by Django 4.1 on 2022-11-27 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0005_alter_hotels_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(upload_to='hotel_images/')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.hotels')),
            ],
            options={
                'verbose_name': 'Дополнительноe фото',
                'verbose_name_plural': 'Дополнительные фотографии',
            },
        ),
    ]