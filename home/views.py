from django.shortcuts import render
from django.http import HttpResponse
from home.models import Introduction
# .models = default place
# Create your views here.

def homeview(request):
    intros = Introduction.objects.all()
    print(intros)
# the name before value are the assigned keys to that value, ex: student_name is key for name.
    return render(request, 'home.html', {'intro' :intros})
