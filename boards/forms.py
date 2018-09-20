from django import forms
import datetime
from .models import Post, Topic
from django.forms.widgets import SelectDateWidget
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
from django.utils import timezone

FRUIT_CHOICES = [
    ('09:00', '09:00'),
    ('09:30', '09:30'),
    ('10:00', '10:00'),
    ('10:30', '10:30'),
    ('11:00', '11:00'),
    ('11:30', '11:30'),
    ('12:00', '12:00'),
    ('12:30', '12:30'),
    ('13:00', '13:00'),
    ('13:30', '13:30'),
    ('14:00', '14:00'),
    ('14:30', '14:30'),
    ('15:00', '15:00'),
    ('15:30', '15:30'),
    ('16:00', '16:00'),
    ('16:30', '16:30'),
    ('17:00', '17:00'),
    ('17:30', '17:30'),
]

FRUIT_CHOICES2 = [
    ('09:30', '09:30'),
    ('10:00', '10:00'),
    ('10:30', '10:30'),
    ('11:00', '11:00'),
    ('11:30', '11:30'),
    ('12:00', '12:00'),
    ('12:30', '12:30'),
    ('13:00', '13:00'),
    ('13:30', '13:30'),
    ('14:00', '14:00'),
    ('14:30', '14:30'),
    ('15:00', '15:00'),
    ('15:30', '15:30'),
    ('16:00', '16:00'),
    ('16:30', '16:30'),
    ('17:00', '17:00'),
    ('17:30', '17:30'),
    ('18:00', '18:00'),
]

ROOM_CHOICE = [
    ('room1', 'room1'),
    ('room2', 'room2'),
]


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': ''}
        ),
        max_length=4000,
        help_text='Guests, extra information etc.'
    )

    start_time = forms.TimeField(widget=forms.Select(choices=FRUIT_CHOICES))
    end_time = forms.TimeField(widget=forms.Select(choices=FRUIT_CHOICES2))
    room = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    #room = forms.CharField(widget=forms.Select(choices=ROOM_CHOICE))
    day = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'), initial=datetime.date.today)

    class Meta:
        model = Topic
        fields = ['subject', 'message', 'day', 'start_time', 'end_time', 'room']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = []


class QueryForm(forms.ModelForm):
    day = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'), label='Search reservation for any date:',
                          initial=datetime.date.today)

    class Meta:
        model = Topic
        fields = ['day']
