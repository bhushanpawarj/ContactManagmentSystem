"""
Definition of views.
"""
from .serializers import ContactsSerializer
from django.db.models import Count
from django.shortcuts import redirect
from django.http import JsonResponse

import json 
from django.http import JsonResponse
from django.http import HttpResponse
from django.forms.models import model_to_dict


from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
#importing model to fetch the reocords
from app.models import Contacts ,Address,Phone,Date
from .forms import ContactForm,AddressForm,PhoneForm,DateForm
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    #AllContacts=Contacts.objects.all()
    #AllContacts=Address.objects.all().prefetch_related('Contact_id__')[:10]

    #to add pagination support
    AllContacts = Contacts.objects.all().order_by('-pk')[:10]
    #paginator = Paginator(AllContacts, 20) # Show 25 contacts per page

    #page = request.GET.get('page')
    #contacts = paginator.get_page(page)
    #data=serializers.serialize("json", AllContacts)


    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'AllContacts':AllContacts,
        }
    )
def CreateContact(request):
    form=ContactForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request ,'app/CreateContactForm.html', {'form' : form })

def UpdateContact(request,pk):
    Contact=Contacts.objects.get(id=pk)
    AllAddress=Address.objects.filter(Contact_id=pk)
    AllPhones=Phone.objects.filter(Contact_id=pk)
    AllDates=Date.objects.filter(Contact_id=pk)

    form=ContactForm(request.POST or None ,instance=Contact)
    #addressform=AddressForm(request.POST or None ,instance=Contact)
    if form.is_valid():
        form.save()
        #addressform.save()
        #return redirect('home')

    return render(request ,'app/ContactEdit.html', {'form' : form ,'Contact':Contact,'AllAddress' : AllAddress ,'AllPhones' :AllPhones,'AllDates':AllDates })

def RetriveJson(request):
    #Contact=Contacts.objects.filter(pk=pk)
    Contact=Contacts.objects.all().select_related('addresses')
    serializedData=ContactsSerializer(Contact,many=True)
    

    return JsonResponse(serializedData.data,safe=False)
def GetContactsData(request):
    #Contact=Contacts.objects.filter(pk=pk)
    Contact=Contacts.objects.all()
    serializedData=ContactsSerializer(Contact,many=True)
  
    return JsonResponse(serializedData.data,safe=False)


def UpdateAddress(request):
    AddressId=request.POST['AddressId']
    AddressToSave=Address.objects.get(pk=AddressId)
    AddressToSave.Address_type=request.POST['Address_type']
    AddressToSave.Address=request.POST['Address']
    AddressToSave.City=request.POST['City']
    AddressToSave.State=request.POST['State']
    AddressToSave.Zip=request.POST['Zip']
    try:
        AddressToSave.save()
    except e:
        print(e)


         #SaveOrNot=True
    # except:
        #SaveOrNot=False


    return HttpResponse('')
    #return render(request ,'app/ContactEdit.html', {'SaveOrNot' : SaveOrNot})

def DeleteContact(request,pk):
    Contact=Contacts.objects.get(id=pk)
    Contact.delete()
    return redirect('home')

def EditContact(request,pk):
     Contact = Contacts.objects.get(pk=pk)
     AllAddress=Address.objects.filter(Contact_id=pk)
     AllPhones=Phone.objects.filter(Contact_id=pk)
     AllDates=Date.objects.filter(Contact_id=pk)

     return render(
        request,
        'app/ContactEdit.html',
        {
            'Contact':Contact,
            'AllAddress' : AllAddress,
            'AllPhones':AllPhones,
            'AllDates':AllDates,
        }
    )
def SaveContact(request,Fname,Mname,Lname,pk=None):
        try:
            Contact=Contacts.objects.filter(pk=pk)
            Contact.Fname=Fname
            Contact.Mname=Mname
            Contact.Lname=Lname
            Contact.save()
            isContactSuccessfull=1
        except:
            isContactSuccessfull=0


        return render(
            request,
            'app/ContactEdit.html',
            {
                'isContactSuccessfull':isContactSuccessfull,
            }
        )


def loadData(request):
    AllContacts = Contacts.objects.all()
    dataTOConvert=model_to_dict(AllContacts)
    data = serializers.serialize('json', AllContacts)
    return HttpResponse(data, content_type='application/json')
    #return JsonResponse(json.dumps(data, encoding='UTF-8'), safe=False)


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
