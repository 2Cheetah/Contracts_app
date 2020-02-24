from django.urls import path
from .views import ContractListView
from . import views


urlpatterns = [
    path('', ContractListView.as_view(), name='contracts-home')
]