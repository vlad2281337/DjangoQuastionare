from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User, Appointment, Doctor


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'role']


class CreateNewAppointment(forms.ModelForm):
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all())
    date = forms.DateField(widget=forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                       'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
                      }))
    time = forms.TimeField(widget=forms.TimeInput(
                attrs={'class': 'form-control',
                       'type': 'time'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
                      }))
    complains = forms.CharField()
    class Meta:
        model = Appointment
        fields = ['doctor', 'date', 'time', 'complains']


class DetailAppointment(forms.ModelForm):
    symptoms = forms.CharField()
    diagnosys = forms.CharField()
    recomendations = forms.CharField()

    class Meta:
        model = Appointment
        fields = ['symptoms', 'diagnosys', 'recomendations']


