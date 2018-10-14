"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from .models import Contacts,Address,Phone,Date
class ContactForm(forms.ModelForm):
    class Meta:
        model=Contacts
        fields =['id','Fname' ,'Mname' ,'Lname']

        def __init__(self ,*args,**kwargs):
            super(ContactForm,self).__init__(*args,**kwargs)
            self.fields['description'].widget=TextInput(attrs={
            'class': 'form-control',
            })

class AddressForm(forms.ModelForm):
    class Meta:
        model=Address
        fields =[ 'Contact_id','id' , 'Address_type' ,'Address','City','State','Zip']

class PhoneForm(forms.ModelForm):
    class Meta:
        model=Phone
        fields =['Contact_id' ,'Phone_type' ,'Area_code','Number']

class DateForm(forms.ModelForm):
    class Meta:
        model=Date
        fields =['Contact_id' ,'Date_type' ,'Date']

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
