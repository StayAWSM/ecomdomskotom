from django.urls import path
from .views import ContactCreate, home_page, index

urlpatterns = [
    path('contact/', ContactCreate.as_view(), name='contact_form'),
    path('home/', home_page, name='home_page'),
    path('index/', index, name='index')
]
