from django.shortcuts import render

from .models import Puncher

def dashboard(request):
    user = Puncher.objects.get(pk=1)
    username = user.__str__()

    all_projects = list(user.projects_shared.all())

    context = {'username': username, 'all_projects': all_projects}
    return render(request, 'dashboard.html', context)