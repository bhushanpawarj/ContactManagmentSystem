"""
Definition of urls for ContactManagmentSystem.
"""

from datetime import datetime
from django.conf.urls import url
#from django.conf import path
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [

    
    #CRUD FOR CONTACT
    url(r'^New$', app.views.CreateContact, name='NewContact'),
    url(r'^Update/(?P<pk>\d+)/$', app.views.UpdateContact, name='UpdateContact'),
    url(r'^RetriveJson/$', app.views.RetriveJson, name='RetriveJson'),
    url(r'^Delete/(?P<pk>\d+)/$', app.views.DeleteContact, name='DeleteContact'),
    url(r'^Edit/(?P<pk>\d+)/$', app.views.EditContact, name='getAllContactData'),
    
    #CRUD FOR ADDRESS
    url(r'^UpdateAddress/(?P<pk>\d+)/$', app.views.UpdateAddress, name='UpdateAddress'),
    url(r'^DeleteAddress/(?P<pk>\d+)/(?P<ContactId>\d+)$', app.views.DeleteAddress, name='DeleteAddress'),
    url(r'^NewAddress/(?P<ContactId>\d+)$', app.views.NewAddress, name='NewAddress'),

    #CRUD FOR PHONE
    url(r'^UpdatePhone/(?P<pk>\d+)/$', app.views.UpdatePhone, name='UpdatePhone'),
    url(r'^DeletePhone/(?P<pk>\d+)/(?P<ContactId>\d+)$', app.views.DeletePhone, name='DeletePhone'),
    url(r'^NewPhone(?P<ContactId>\d+)/$', app.views.NewPhone, name='NewPhone'),

    #CRUD FOR DATE
    url(r'^UpdateDate/(?P<pk>\d+)/$', app.views.UpdateDate, name='UpdateDate'),
    url(r'^Delete/(?P<pk>\d+)/(?P<ContactId>\d+)$', app.views.DeleteDate, name='DeleteDate'),
    url(r'^NewDate/(?P<ContactId>\d+)$', app.views.NewDate, name='NewDate'),

    #url(r'^SaveContact/(?P<pk>\d+)/$', app.views.SaveContact, name='SaveContact'),
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^search', app.views.search, name='search'),
    url(r'^loadData$', app.views.loadData, name='loadData'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
]
