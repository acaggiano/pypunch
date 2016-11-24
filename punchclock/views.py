from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Project, Profile, Work

def index(request):
  """Home page for PyPunch"""
  return render(request, 'punchclock/index.html')

@login_required
def dashboard(request):
    user = request.user
    username = user.__str__()
    try:
        most_recent_punch = user.profile.work_set.all().latest('time_start')
    except Work.DoesNotExist:
        most_recent_punch = None

    try:
        project_recent_punch = Work.objects.filter(project__creator=user.profile).latest('time_start')
    except Work.DoesNotExist:
        project_recent_punch = None
    try:
        most_recent_share = user.profile.projects_shared.exclude(creator=user.profile).latest('created')
    except Project.DoesNotExist:
        most_recent_share = None
    
    all_projects = Project.objects.filter(creator=request.user.profile).order_by('created')

    context = {'user':user, 'username': username, 'most_recent_punch': most_recent_punch,
               'project_recent_punch': project_recent_punch, 
               'most_recent_share': most_recent_share,
               'all_projects': all_projects
               }
    return render(request, 'punchclock/dashboard.html', context)

@login_required
def projects(request, project_id):
    """Create a page for a project"""
    project = Project.objects.get(id=project_id)
    works = project.work_set.order_by('time_start')
    context = {'project': project, 'works': works}
    return render(request, 'punchclock/project.html', context)