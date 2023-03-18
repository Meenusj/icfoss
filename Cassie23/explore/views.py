from django.shortcuts import render
from .models import Destination

# Create your views here.
def home(request):
    
    return render(request, 'map.html')

def details(request):
    destination=Destination(id=1)
    
    return render(request, 'destinationInfo.html', {"destination":destination})
