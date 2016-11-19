from django.shortcuts import render

from .models import Puncher, Work

def dashboard(request):
    user = Puncher.objects.get(pk=1)
    username = user.__str__()
    most_recent_punch = user.work_set.all().latest('time_start')
    project_recent_punch = Work.objects.filter(
        project__creator=user
    ).latest('time_start')

    all_projects = list(user.projects_shared.all())

    context = {'user':user, 'username': username, 'most_recent_punch': most_recent_punch,
               'project_recent_punch': project_recent_punch, 'all_projects': all_projects}
    return render(request, 'dashboard.html', context)