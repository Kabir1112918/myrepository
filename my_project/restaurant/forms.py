from django.forms import ModelForm
from .models import Booking
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Code added for loading form data on the Booking page
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"



# registration form
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')  # Customize fields as needed
