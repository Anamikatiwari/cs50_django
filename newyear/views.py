from django.shortcuts import render
import datetime

# Create your views here.


def index(request):
    now= datetime.datetime.now()
    return render(request, "newyear/index.html", {
        
        # this below code give the output NO
        "newyear":now.month ==  1 and now.day == 1
        
        # this below code give the output YES
        # "newyear": True
    })
    