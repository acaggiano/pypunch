from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime

from .models import Project, Profile, Work
from .forms import ProjectForm

def index(request):
  """Home page for PyPunch"""
  if request.user.is_authenticated():
      return HttpResponseRedirect(reverse('punchclock:dashboard'))
  else:
      return render(request, 'punchclock/index.html')

@login_required
def dashboard(request):
    user = request.user
    username = user.__str__().capitalize()
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
    paginator = Paginator(all_projects, 3)

    page = request.GET.get('page')
    try:
        all_projects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        all_projects = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page
        all_projects = paginator.page(paginator.num_pages)

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

@login_required
def new_project(request):
    """Add a new project"""
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = ProjectForm()
    else:
        # POST submitted, send data
        form = ProjectForm(request.POST)
        if form.is_valid():
            new_project = form.save(commit=False)
            new_project.creator = request.user.profile
            new_project.save()
            return HttpResponseRedirect(reverse('punchclock:dashboard'))

    context = {'form': form}
    return render(request, 'punchclock/new_project.html', context)

@login_required
def edit_project(request, project_id):
    """Edit existing project"""
    project = Project.objects.get(id=project_id)

    if request.method != 'POST':
        form = ProjectForm(instance=project)

    else:
        form = ProjectForm(instance=project, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('punchclock:projects', args=[project_id]))

    context = {'project': project, 'form': form}
    return render(request, 'punchclock/edit_project.html', context)

def punch(request):
    user = request.user
    project = request.POST.get("project","").replace("project-btn-","")
    this_project = Project.objects.get(pk=project)
    punch_status = request.POST.get("punchstatus","")

    if(punch_status == "Out"):
        user_work =  Work.objects.filter(worker__user=user,project__id=project).latest('time_start')
        user_work.time_end = datetime.datetime.now()
        user_work.save()
    else:
        new_work = Work.objects.create(worker=user.profile,
                                       project=this_project,
                                       time_start = datetime.datetime.now()
        )

    return HttpResponse(this_project)