from django.shortcuts import render
from .forms import RegisterForm
from django.shortcuts import render
from django.shortcuts import redirect

def authview(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('airport')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form':form})