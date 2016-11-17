from django.db import models
from django.contrib.auth.models import User


class Puncher(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        """Returns string with name"""
        return self.user.get_username()


class Project(models.Model):
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(Puncher, related_name="projects_created")
    created = models.DateTimeField(auto_now_add=True)
    shared_with = models.ManyToManyField(Puncher, related_name="projects_shared", blank=True)
    contributors = models.ManyToManyField(Puncher, through="Work", related_name="project_contributors")

    def __str__(self):
        """Returns string with name"""
        return self.name


class Work(models.Model):
    worker = models.ForeignKey(Puncher)
    project = models.ForeignKey(Project)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()

    def __str__(self):
        """Return string with work info"""
        return self.worker.__str__() + " | " + self.project.__str__() + ": "+ self.time_start.__str__()\
               + " - " + self.time_end.__str__()
