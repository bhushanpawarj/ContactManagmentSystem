from rest_framework_dyn_serializer import serializers
from .models import Contacts,Address

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contacts
        fields=('id','Fname','Mname','Lname')

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=Address
        fields=('Address_Id','Address','State','City')


