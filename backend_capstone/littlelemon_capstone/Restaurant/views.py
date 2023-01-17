from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import MenuSerializer, BookingSerializer
from .models import Menu, Bookings
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render(request, "index.html", {})

class MenuItemsView(generics.ListCreateAPIView):
    serializer_class = MenuSerializer
    model = Menu
    queryset = Menu.objects.all()

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    serializer_class = MenuSerializer
    model = Menu
    queryset = Menu.objects.all()

class BookingsViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    model = Bookings
    queryset = Bookings.objects.all()
    permission_classes = [IsAuthenticated]