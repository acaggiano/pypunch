from django.shortcuts import render

from .models import Puncher

def dashboard(request):
    user = Puncher.objects.get(pk=1)
    username = user.__str__()
    context = {'username': username}
    return render(request, 'dashboard.html', context)