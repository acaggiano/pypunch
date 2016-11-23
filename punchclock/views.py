from django.shortcuts import render

from .models import Puncher, Work

def index(request):
  """Home page for PyPunch"""
  return render(request, 'punchclock/index.html')

def dashboard(request):
    user = request.user
    username = user.__str__()
    #most_recent_punch = user.work_set.all().latest('time_start')
    #project_recent_punch = Work.objects.filter(project__creator=user).latest('time_start')
    #most_recent_share = user.projects_shared.exclude(creator=user).latest('created')

    #all_projects = list(user.projects_shared.all())

    context = {'user':user, 'username': username, #'most_recent_punch': most_recent_punch,
               #'project_recent_punch': project_recent_punch, 'most_recent_share': most_recent_share,
               #'all_projects': all_projects
               }
    return render(request, 'punchclock/dashboard.html', context)