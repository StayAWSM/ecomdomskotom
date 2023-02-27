from django.forms import ModelForm, Textarea
from .models import Contact, Booking
from django import forms


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'message']
        widgets = {
            'message': Textarea(
                attrs={'plaсeholder': 'Напишите сюда обращение...'}
            )
        }


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date'}
            )
        }
