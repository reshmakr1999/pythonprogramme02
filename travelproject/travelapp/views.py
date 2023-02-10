from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import  person



# Create your views here.
def demo(request):
    obj=Place.objects.all()
    abj=person.objects.all()
    return render(request, "index.html",{'result':obj,'results':abj})


