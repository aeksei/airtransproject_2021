# serializers.py

from rest_framework import serializers

from airtrans.models import Booking, Ticket, Flight, BoardingPass, TicketFlight


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking

        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket

        fields = (
            'ticket_no',
            'book_ref',
        )


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight

        fields = "__all__"


class TicketFlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketFlight

        fields = "__all__"


class BoardingPassSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardingPass

        fields = "__all__"