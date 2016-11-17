# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 03:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Puncher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_start', models.DateTimeField()),
                ('time_end', models.DateTimeField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='punchclock.Project')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='punchclock.Puncher')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='contributors',
            field=models.ManyToManyField(related_name='project_contributors', through='punchclock.Work', to='punchclock.Puncher'),
        ),
        migrations.AddField(
            model_name='project',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects_created', to='punchclock.Puncher'),
        ),
        migrations.AddField(
            model_name='project',
            name='shared_with',
            field=models.ManyToManyField(related_name='projects_shared', to='punchclock.Puncher'),
        ),
    ]
