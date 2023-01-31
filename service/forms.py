from django.forms import ModelForm, Textarea
from .models import Contact


class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'message']
        widgets = {
            'message': Textarea(
                attrs={'plaсeholder': 'Напишите сюда обращение...'}
            )
        }
