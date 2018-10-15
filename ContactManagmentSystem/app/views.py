"""
Definition of views.
"""
from .serializers import ContactsSerializer
from django.db.models import Count
from django.shortcuts import redirect
from django.http import JsonResponse
from django.db.models import Q
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

    #to add pagination 

    #AllContacts = Contacts.objects.all().order_by('-pk')[:10]
   
   #paginator = Paginator(AllContacts, 20) # Show 25 contacts per page

    #page = request.GET.get('page')
    #contacts = paginator.get_page(page)
    #data=serializers.serialize("json", AllContacts)

    AllContacts = Contacts.objects.all()
    query=request.GET.get("query")
    if query:
        AllContacts=AllContacts.filter(
            Q(Fname__icontains=query)|
            Q(Mname__icontains=query)|
            Q(Lname__icontains=query)|
            Q(addresses__Address__icontains=query)|
            Q(addresses__City__icontains=query)|
            Q(addresses__State__icontains=query)|
            Q(addresses__Zip__icontains=query)|
            Q(phones__Area_code__icontains=query)|
            Q(phones__Number__icontains=query)|
            Q(dates__Date__icontains=query)           
            ).distinct()
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'AllContacts':AllContacts,
        }
    )

def search(request,searchText=None):
   
    for searchResult in Contacts.objects.raw('select * from  app_contacts AC join app_date AD where AD.Contact_id_id=AC.id'):
        print(searchResult)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'searchResult':searchResult,
        }
    )



def CreateContact(request):


    form=ContactForm(request.POST or None )
    if form.is_valid():
        form.save()
    return render(request ,'app/ContactEdit.html', {'form' : form  })

def UpdateContact(request,pk):
    Contact=Contacts.objects.get(id=pk)
    AllAddress=Address.objects.filter(Contact_id=pk)
    AllPhones=Phone.objects.filter(Contact_id=pk)
    AllDates=Date.objects.filter(Contact_id=pk)

    form=ContactForm(request.POST or None ,instance=Contact)
    if form.is_valid():
        form.save()
        #addressform.save()
        #return redirect('home')

    return render(request ,'app/ContactEdit.html', {'form' : form ,'Contact':Contact,'AllAddress' : AllAddress ,'AllPhones':AllPhones,'AllDates':AllDates })

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

def NewAddress(request,ContactId):
    add=Address()
    contact=Contacts.objects.get(pk=ContactId)
    add.Contact_id=contact
    form=AddressForm(request.POST or None ,instance=add)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request ,'app/CreateContactForm.html', {'form' : form })

def NewPhone(request,ContactId):
    ph=Phone()
    contact=Contacts.objects.get(pk=ContactId)
    ph.Contact_id=contact
    form=PhoneForm(request.POST or None )
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request ,'app/CreateContactForm.html', {'form' : form })

def NewDate(request,ContactId):
    dt=Date()
    contact=Contacts.objects.get(pk=ContactId)
    dt.Contact_id=contact
    form=DateForm(request.POST or None )
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request ,'app/CreateContactForm.html', {'form' : form })


def UpdateAddress(request,pk):
    Add=Address.objects.get(id=pk)
    form=AddressForm(request.POST or None ,instance=Add)
    if form.is_valid():
        form.save()
    return render(request ,'app/AddOrUpdateAddress.html', {'form' : form ,'Address':Add})

def UpdatePhone(request,pk):   
    Ph=Phone.objects.get(id=pk)
    form=PhoneForm(request.POST or None ,instance=Ph)
    if form.is_valid():
        form.save()
    return render(request ,'app/AddOrUpdateAddress.html', {'form' : form ,'Address':Ph})
def UpdateDate(request,pk):
    
    Dt=Date.objects.get(id=pk)
    form=PhoneForm(request.POST or None ,instance=Dt)
    if form.is_valid():
        form.save()
    return render(request ,'app/AddOrUpdateAddress.html', {'form' : form ,'Address':Dt})

def DeleteAddress(request,pk=None,ContactId=None):
    Add=Address.objects.get(id=pk)
    Add.delete()
    Contact=Contacts.objects.get(id=ContactId)
    form=ContactForm(request.POST or None ,instance=Contact)
    AllAddress=Address.objects.filter(Contact_id=ContactId)
    AllPhones=Phone.objects.filter(Contact_id=ContactId)
    AllDates=Date.objects.filter(Contact_id=ContactId)
    return render(request ,'app/ContactEdit.html', {'form' : form ,'Contact':Contact,'AllAddress' : AllAddress ,'AllPhones':AllPhones,'AllDates':AllDates })


def DeletePhone(request,pk=None,ContactId=None):
    Ph=Phone.objects.get(id=pk)
    Ph.delete()
    Contact=Contacts.objects.get(id=ContactId)
    form=ContactForm(request.POST or None ,instance=Contact)
    AllAddress=Address.objects.filter(Contact_id=ContactId)
    AllPhones=Phone.objects.filter(Contact_id=ContactId)
    AllDates=Date.objects.filter(Contact_id=ContactId)
    return render(request ,'app/ContactEdit.html', {'form' : form ,'Contact':Contact,'AllAddress' : AllAddress ,'AllPhones':AllPhones,'AllDates':AllDates })

def DeleteDate(request,pk=None,ContactId=None):
    Dt=Date.objects.get(id=pk)
    Dt.delete()
    Contact=Contacts.objects.get(id=ContactId)
    form=ContactForm(request.POST or None ,instance=Contact)
    AllAddress=Address.objects.filter(Contact_id=ContactId)
    AllPhones=Phone.objects.filter(Contact_id=ContactId)
    AllDates=Date.objects.filter(Contact_id=ContactId)
    return render(request ,'app/ContactEdit.html', {'form' : form ,'Contact':Contact,'AllAddress' : AllAddress,'AllPhones':AllPhones,'AllDates':AllDates  })



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
