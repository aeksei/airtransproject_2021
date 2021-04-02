from rest_framework import routers

from .views import BookingViewSet, TicketViewSet, TicketFlightViewSet, BoardingPassViewSet

router = routers.SimpleRouter()

router.register('bookings', BookingViewSet)
router.register('tickets', TicketViewSet)
router.register('ticket_flights', TicketFlightViewSet)
router.register('pass', BoardingPassViewSet)

urlpatterns = router.urls
print(urlpatterns)
