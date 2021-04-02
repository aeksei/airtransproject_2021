# Generated by Django 3.0.4 on 2020-03-11 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('airport_code', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('airport_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('book_ref', models.AutoField(primary_key=True, serialize=False)),
                ('book_date', models.DateField(auto_now_add=True)),
                ('total_amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('flight_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('arrival_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival_airport', to='airtrans.Airport')),
                ('departure_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure_airport', to='airtrans.Airport')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticket_no', models.AutoField(primary_key=True, serialize=False)),
                ('book_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airtrans.Booking')),
            ],
        ),
        migrations.CreateModel(
            name='TicketFlight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fare_conditions', models.CharField(max_length=100)),
                ('flight_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airtrans.Flight')),
                ('ticket_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airtrans.Ticket')),
            ],
            options={
                'unique_together': {('ticket_no', 'flight_id')},
            },
        ),
    ]