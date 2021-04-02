from django.db import models


class Booking(models.Model):
    book_ref = models.AutoField(primary_key=True)
    book_date = models.DateField(null=False,
                                 blank=False)
    total_amount = models.FloatField()

    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"

    def __str__(self):
        return f"Booking {self.book_ref} - {self.book_date}"


class Ticket(models.Model):
    ticket_no = models.AutoField(primary_key=True)
    book_ref = models.ForeignKey(Booking,
                                 on_delete=models.PROTECT)

    def __str__(self):
        return f"Ticket id: {self.ticket_no}"


class TicketFlight(models.Model):
    ticket_no = models.ForeignKey(Ticket,
                                  on_delete=models.CASCADE)
    flight_id = models.ForeignKey("Flight",
                                  on_delete=models.CASCADE)

    class Meta:
        unique_together = (('ticket_no', 'flight_id'), )

    def __str__(self):
        return f"TicketFlight {self.ticket_no} - {self.flight_id}"


class Flight(models.Model):
    flight_id = models.AutoField(primary_key=True)
    departure_airport = models.ForeignKey("Airport",
                                          on_delete=models.SET_NULL,
                                          null=True,
                                          related_name='dep')
    arrival_airport = models.ForeignKey("Airport",
                                        on_delete=models.SET_NULL,
                                        null=True,
                                        related_name='arr')

    def __str__(self):
        return f"Flight id: {self.flight_id} {self.departure_airport}"


class BoardingPass(models.Model):
    pass_id = models.OneToOneField(TicketFlight,
                                   on_delete=models.CASCADE)
    boarding_no = models.PositiveIntegerField()

    def __str__(self):
        return f"Посадочный талон билета № {self.pass_id.ticket_no} " \
               f"рейса {self.pass_id.flight_id}"


class Airport(models.Model):
    airport_code = models.CharField(max_length=3, primary_key=True)
    ...

    timezone = models.IntegerField(blank=True, null=True)


if __name__ == '__main__':
    queryset_ticket_flight = TicketFlight.objects.filter(flight_id__departure_airport__airport_code='DME')
    queryset_pass = BoardingPass.objects.filter(
        pass_id__flight_id__departure_airport="DME")