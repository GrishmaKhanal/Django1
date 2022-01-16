from django.db.models.fields import PositiveIntegerRelDbTypeMixin
from django.shortcuts import redirect, render
from .models import *
from .forms import *
# Create your views here.
def destination_view(request, id_val):
    check = destination.objects.get(id=id_val)
    return render(request, 'destination.html', {'obj':check})

def airportview(request):
    check1 = airport.objects.all()
    return render(request, 'destination.html', {'obje': check1})

def addview(request):
    form = destform()
    if request.method == 'POST':
        print('not me')
        form = destform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('airport')
    return render(request, 'addview.html', {'form' : form})

def update_destination(request, did):
    dest = airport.objects.get(id =did)
    form = destform(instance=dest)
    if request.method == 'POST':
        form = destform(request.POST, instance=dest)
        if form.is_valid:
            form.save()
            return redirect('airport')
    return render(request, 'updateDest.html',{'form': form})

def delete_airport(request, did):
    dest = airport.objects.get(id = did)
    dest.delete()
    return redirect('airport')  