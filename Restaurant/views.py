from django.shortcuts import render
from rest_framework import viewsets
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer


# Create your views here.
def index(request):
    return render(request, "index.html", {})


class BookingViewSet(viewsets.ModelViewSet):
     queryset = Booking.objects.all()
     serializer_class = BookingSerializer


class MenuViewSet(viewsets.ModelViewSet):
     queryset = Menu.objects.all()
     serializer_class = MenuSerializer

