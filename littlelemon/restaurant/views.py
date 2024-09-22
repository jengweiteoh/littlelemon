from django.shortcuts import render, HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated
from .forms import BookingForm
from django.core import serializers
from datetime import datetime

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'index.html', {})

def menu(request):
    menu_data = MenuItem.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})

def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = MenuItem.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 

# class MenuItemView(ListCreateAPIView):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer

# class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
#     serializer_class = MenuItemSerializer
#     queryset = MenuItem.objects.all()
    
# class BookingViewSet(ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer


def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    # return HttpResponse(context)
    return render(request, 'book.html', context)

def bookings(request):
    date = request.GET.get('date', datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, "bookings.html", {"bookings": booking_json})