from django.shortcuts import render

# Create your views here.
from apps.users.forms import CreateUserForm


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if not form.is_valid():
            
        form.save()

    return render(request, 'register.html')
