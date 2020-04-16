from django import forms
from .models import *

class CreateUserForm(forms.ModelForm):
    name = forms.CharField(
        widget = forms.TextInput(),
        label = "First Name",
        max_length=150,
        help_text='Input your first name',
        required = True
    )
    last_name = forms.CharField(
        widget = forms.TextInput(),
        label = "Last Name",
        max_length=150,
        help_text='Input your last name',
        required = True
    )   
    email = forms.CharField(
        widget = forms.EmailInput(),
        label = "Email",
        max_length=150,
        help_text='Please enter your email',
        required = True
    )   
    password = forms.CharField(
        widget = forms.PasswordInput(),
        label = "Password",
        max_length=150,
        help_text='Please enter password',
        required = True
    )
    rate = forms.DecimalField(
        widget = forms.NumberInput(),
        label = "Rates",
        required = True,
        max_digits=4,
        decimal_places=2
    )
    user_type = forms.ChoiceField(
        choices = User.USER_TYPES,
        label = "Type",
        required = True
    )
    class Meta:
        model = User
        fields = ['name', 
                  'last_name',
                  'email',
                  'password',
                  'rate',
                  'user_type']


class CreateWorkForm(forms.ModelForm):

    hours = forms.IntegerField(
        widget = forms.NumberInput(),
        label = "Hours",
        required = True,
        help_text = "Input the hours you worked on"
    )
    work_type = forms.ChoiceField(
        choices = Work.WORK_TYPE,
        label = "Work Type",
        required = True,
        help_text = "Type of Work You did"
    )
    month = forms.IntegerField(
        widget = forms.NumberInput(),
        label = "Month",
        required = True,
        help_text = "Month"
        )
    notes = forms.CharField(
        widget = forms.TextInput(),
        label = "Notes",
        required = True,
        help_text = "Input the hours you worked on"
        )
    
    class Meta:
        model = Work
        fields = ['hours', 
                  'work_type',
                  'month',
                  'notes'
                  ]
