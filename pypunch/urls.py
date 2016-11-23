from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'', include('punchclock.urls', namespace='punchclock')),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^admin/', admin.site.urls),
]
