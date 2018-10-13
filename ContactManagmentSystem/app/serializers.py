from rest_framework_dyn_serializer import serializers
from .models import Contacts,Address

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contacts
        fields=('Fname','Mname','Lname')

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=Address
        fields=('Address','State','City')


