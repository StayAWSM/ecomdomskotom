from django.urls import path
from .views import ContactCreate, home_page

urlpatterns = [
    path('', ContactCreate.as_view(), name='contact_form'),
    path('/home', home_page, name='home_page'),
]
