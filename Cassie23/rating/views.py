from django.shortcuts import render

# Create your views here.
def home(request):
    a=["1.how likely was the staffs behaviour",
    "2.how was the toilet facility and cleanliness",
    "3.Did accomadation facility is easily available in there",
    "4.did tthere is any hospital facility"]
    return render(request, 'rating.html', {'a':a})


