# Generated by Django 3.1.5 on 2021-03-31 12:59

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('bookingID', models.AutoField(primary_key=True, serialize=False)),
                ('bookingDate', models.DateField(default=datetime.date.today)),
                ('bookingTimeSlot', models.CharField(choices=[('1', '9.30 am - 10.00am'), ('2', '10.00 am - 10.30am'), ('3', '10.30 am - 11.00am'), ('4', '11.00 am - 11.30am'), ('5', '11.30 am - 12.00pm'), ('6', '2.00 pm - 2.00 pm'), ('7', '2.30 pm - 3.00 pm')], max_length=300)),
                ('bookingPatient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('bookingDate', 'bookingTimeSlot')},
            },
        ),
    ]
