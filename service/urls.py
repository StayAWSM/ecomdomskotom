from .views import ContactCreate, CreateBooking, BookingViewSet
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'booking', BookingViewSet)

urlpatterns = [
    path('', ContactCreate.as_view(), name='contact_form'),
    path('home/', CreateBooking.as_view(), name='home_page'),

    # API
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework'))
]
