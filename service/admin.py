from django.contrib import admin
from .models import Contact, Booking


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'message')
    list_display_links = ('email',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time_from',
                    'time_to', 'table_number')
    list_display_links = ('name',)
