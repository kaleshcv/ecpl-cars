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

    print(jsondata)


