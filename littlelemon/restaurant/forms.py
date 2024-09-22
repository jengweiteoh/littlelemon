from .models import Booking
from django import forms

class BookingForm(forms.ModelForm):
    booking_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'}))
    class Meta:
        model = Booking
        fields = "__all__"