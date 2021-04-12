from django.shortcuts import render
from django.http import HttpResponse

import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Create your views here.


def indexPage(request):
    return render(request,'index.html')


@csrf_exempt
@require_POST

def webhook(request):
    jsondata=request.body

    #data=json.loads(jsondata)

    #print(data)

    endpoint = 'https://api.hubapi.com/contacts/v1/contact/?hapikey=a41d69da-80ea-4bec-ad26-efe730f9c7d2'
    headers = {}

    headers["Content-Type"] = "application/json"


    r = requests.post(url=endpoint, data=jsondata, headers=headers)

    print(r.text)

    return HttpResponse(status=200)

def findParts(request):
    if request.method== 'POST':
        make=request.POST['make']
        model=request.POST['model']
        part= request.POST['part']
        year=request.POST['year']

        data={'make':make,'model':model,'part':part,'year':year}

        return render(request,'find-parts.html',data)

    else:
        pass

def thanksPage(request):

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
          "value": "testingapis@hubspot.com"
        },
        {
          "property": "firstname",
          "value": "test"
        },
        {
          "property": "lastname",
          "value": "testerson"
        },
        {
          "property": "website",
          "value": "http://hubspot.com"
        },
        {
          "property": "company",
          "value": "HubSpot"
        },
        {
          "property": "phone",
          "value": "555-122-2323"
        },
        {
          "property": "address",
          "value": "25 First Street"
        },
        {
          "property": "city",
          "value": "Cambridge"
        },
        {
          "property": "state",
          "value": "MA"
        },
        {
          "property": "zip",
          "value": "02139"
        }
      ]
    })


    r = requests.post( url = endpoint, data = data, headers = headers )

    print(r.text)