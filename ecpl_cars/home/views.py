from django.shortcuts import render
from django.http import HttpResponse

import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import *

# Create your views here.


def indexPage(request):
    return render(request,'index.html')

def aboutUs(request):
    return render(request,'about-us.html')

def customerService(request):
    return render(request,'customer-service.html')

def partRequest(request):
    return render(request,'parts-request.html')

@csrf_exempt
@require_POST

def webhook(request):

    if request.method == 'POST':
        jsondata=request.body
        print(jsondata)
        return HttpResponse(status=200)

    else:
        pass


def findParts(request):
    if request.method== 'POST':
        make=request.POST['make']
        part= request.POST['part']
        year=request.POST['year']

        data={'make':make,'part':part,'year':year}

        return render(request,'find-parts.html',data)

    else:
        pass

def thanksPage(request):

    if request.method=='POST':
        customer_name=request.POST['name']
        customer_email=request.POST['email']
        customer_phone=request.POST['phone']
        customer_zip = request.POST['zip']
        year=request.POST['year']
        make_model = request.POST['make']
        part = request.POST['part']

        lead = Leads.objects.create(customer_name=customer_name,customer_email=customer_email,
                                    customer_phone=customer_phone,customer_zip=customer_zip,
                                    year=year,make_model=make_model,part=part)
        lead.save()

        '''p1 = {
            "property": "email",
            "value": email}
        p2 = {
            "property": "firstname",
            "value": name}

        p3 = {
            "property": "phone",
            "value": phone}

        p4 = {
            "property": "year",
            "value": year}

        endpoint = 'https://api.hubapi.com/contacts/v1/contact/?hapikey=a41d69da-80ea-4bec-ad26-efe730f9c7d2'
        headers = {}
        headers["Content-Type"] = "application/json"
        data = json.dumps({
            "properties": [p1,p2,p3]
        })

        r = requests.post(url=endpoint, data=data, headers=headers)'''

    else:
        pass


    return render(request, 'thanks-page.html')


import requests
import json

def hubspotTest(request):

    endpoint = 'https://api.hubapi.com/contacts/v1/contact/?hapikey=a41d69da-80ea-4bec-ad26-efe730f9c7d2'
    headers = {}
    headers["Content-Type"]="application/json"
    data = json.dumps({
      "properties": [
        {
          "property": "email",
          "value": "kaleshcv2@gmail.com"
        },
        {
          "property": "firstname",
          "value": "kalesh"
        },
        {
          "property": "lastname",
          "value": "cv"
        },
        {
          "property": "website",
          "value": "http://ecpl.com"
        },
        {
          "property": "company",
          "value": "ECPL"
        },
        {
          "property": "phone",
          "value": "112333444"
        },
        {
          "property": "address",
          "value": "test"
        },
        {
          "property": "city",
          "value": "Cambridge"
        },
        {
          "property": "state",
          "value": "CA"
        },
        {
          "property": "zip",
          "value": "1234"
        }
      ]
    })


    r = requests.post( url = endpoint, data = data, headers = headers )

    #print(r.text)

def resourcesPage(request):

    return render(request,'resources.html')

def blogOne(request):
    return render(request,'blog-1.html')

def blogTwo(request):
    return render(request,'blog-2.html')

def blogThree(request):
    return render(request,'blog-3.html')
