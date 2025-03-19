from django.urls import path
from .views import main_port_index, about_me_index, contact_index
app_name = 'main_port'
urlpatterns = [
    path('', main_port_index, name='home'),
    path('about_me/', about_me_index, name='about'),
    path('contact/', contact_index, name='contact'),
]
