from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Create your views here.


def indexPage(request):
    return render(request,'index.html')


@csrf_exempt
@require_POST

def webhook(request):
    jsondata=request.body
    data={'text':jsondata}

    print(jsondata)
    return render(request,'sample-chat.html',data)

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
