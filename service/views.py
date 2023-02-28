from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import ContactForm, BookingForm
from .models import Contact, Booking
from rest_framework import viewsets
from .serializers import BookingSerializer


class ContactCreate(CreateView):
    model = Contact
    # fields = ['name', 'email', 'message']
    success_url = reverse_lazy('home_page')
    form_class = ContactForm
    template_name = 'service/contact_form.html'


class CreateBooking(CreateView):
    form_class = BookingForm
    model = Booking
    # fields = '__all__'
    template_name = 'service/home.html'
    success_url = reverse_lazy('home_page')


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
