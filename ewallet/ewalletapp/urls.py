from django.urls import path
from . import views

urlpatterns = [
    path('balance-transfer/', views.balance_transfer, name='balance_transfer'),
    path('transaction-history/', views.transaction_history, name='transaction_history'),
]