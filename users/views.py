from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm

def login_view(request, **kwargs):
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('punchclock:dashboard'))
	else:
		return auth_views.login(request, **kwargs)

def logout_view(request):
	"""Log the user out"""
	logout(request)
	return HttpResponseRedirect(reverse('punchclock:index'))

def register(request):
	"""Register a new user"""
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('punchclock:dashboard'))
	else:
		if request.method !='POST':
			# Display blank registration
			form = UserCreationForm()
		else:
			#Process form
			form = UserCreationForm(data=request.POST)

			if form.is_valid():
				new_user = form.save()
				#log the user in and redirect to dashboard
				authenticated_user = authenticate(username=new_user.username,
					password=request.POST['password1'])
				login(request, authenticated_user)
				return HttpResponseRedirect(reverse('punchclock:dashboard'))

		context = {'form': form}
		return render(request, 'users/register.html', context)

	