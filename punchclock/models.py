from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    
    def __str__(self):
        """Returns string with name"""
        return self.user.get_username()


class Project(models.Model):
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(Profile, related_name="projects_created")
    created = models.DateTimeField(auto_now_add=True)
    shared_with = models.ManyToManyField(Profile, related_name="projects_shared", blank=True)
    contributors = models.ManyToManyField(Profile, through="Work", related_name="project_contributors")

    def __str__(self):
        """Returns string with name"""
        return self.name


class Work(models.Model):
    worker = models.ForeignKey(Profile)
    project = models.ForeignKey(Project)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        """Return string with work info"""
        return self.worker.__str__() + " | " + self.project.__str__() + ": "+ self.time_start.__str__()\
               + " - " + self.time_end.__str__()
