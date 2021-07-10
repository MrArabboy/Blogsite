from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'users/register.html',{'register_form':form})
