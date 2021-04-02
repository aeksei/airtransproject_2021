from django.db import models

# Create your models here.


class Booking(models.Model):

    book_ref = models.AutoField(primary_key=True)
    book_date = models.DateField(auto_now_add=True)
    total_amount = models.FloatField(null=False)

    def __str__(self):
        return "{}".format(self.book_ref)


class Ticket(models.Model):
    ticket_no = models.AutoField(primary_key=True)
    book_ref = models.ForeignKey(Booking,
                                 on_delete=models.CASCADE)


class Airport(models.Model):

    airport_code = models.CharField(max_length=4,
                                    primary_key=True)
    airport_name = models.CharField(max_length=50)


class Flight(models.Model):
    flight_id = models.PositiveIntegerField(primary_key=True)
    departure_airport = models.ForeignKey(Airport,
                                          related_name='departure_airport',
                                          on_delete=models.CASCADE)
    arrival_airport = models.ForeignKey(Airport,
                                        related_name='arrival_airport',
                                        on_delete=models.CASCADE)

    def save(self, *args, **kwags):

        super().save(*args, **kwags)

class TicketFlight(models.Model):
    ticket_no = models.ForeignKey(Ticket,
                                  on_delete=models.CASCADE)
    flight_id = models.ForeignKey(Flight,
                                  on_delete=models.CASCADE)
    fare_conditions = models.CharField(max_length=100)

    class Meta:
        unique_together = (
            ('ticket_no', 'flight_id'),
        )


class BoardingPass(models.Model):
    pass_id = models.OneToOneField(TicketFlight,
                                   on_delete=models.CASCADE)
    boarding_no = models.PositiveIntegerField()

    def __str__(self):
        return f"Посадочный талон билета № {self.pass_id.ticket_no} " \
               f"рейса {self.pass_id.flight_id}"