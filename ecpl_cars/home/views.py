from django.shortcuts import render
from django.http import HttpResponse

import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Create your views here.


def indexPage(request):
    return render(request,'index.html')

def aboutUs(request):
    return render(request,'about-us.html')

def customerService(request):
    return render(request,'customer-service.html')


@csrf_exempt
@require_POST

def webhook(request):

    jsondata=request.body

    data=json.loads(jsondata)
    print('-------------------------------')
    #print(data['pre_chat_survey'])
    datalist=data['pre_chat_survey']
    contact_list=[]
    for i in datalist:
        print(i['answer'])
        contact_list.append(i['answer'])

    print(contact_list)

    p1={"property": "email",
          "value": contact_list[1]}
    p2={
          "property": "firstname",
          "value": contact_list[0]
        }
    p3={
          "property": "phone",
          "value": contact_list[2]
        }

    data_to_dump={'properties':[p1,p2,p3]}

    print('----------------')
    print(data_to_dump)

    endpoint = 'https://api.hubapi.com/contacts/v1/contact/?hapikey=a41d69da-80ea-4bec-ad26-efe730f9c7d2'
    headers = {}
    headers["Content-Type"] = "application/json"
    data = json.dumps(data_to_dump)

    r = requests.post(url=endpoint, data=data, headers=headers)

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

    print(r.text)