from django.urls import path
from .views import qr_code

app_name = 'qr_app'

urlpatterns = [
    path('', qr_code, name='qr_code'),
]