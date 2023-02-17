from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from .models import Contact


class ContactCreate(CreateView):
    model = Contact
    # fields = ['name', 'email', 'message']
    success_url = reverse_lazy('home_page')
    form_class = ContactForm
    template_name = 'service/contact_form.html'


def home_page(request):
    return HttpResponse('<h1>Home_page</h1>')


def index(request):
    return render(request, 'service/index.html')
