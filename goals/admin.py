from django.contrib import admin
from goals.models import *
import datetime


class SubtaskInLine(admin.TabularInline):
  model = SubTask
  extra = 3


class GoalAdmin(admin.ModelAdmin):
  form = GoalForm

  fieldsets = [
    ('Subject', {'fields':['subject']}),
    ('Date Information', {'fields':['deadline']}),
    ('Kredit Reward', {'fields':['kredit_reward']}),
  ]
#  fields = ['subject','pub_date','kredit_reward','deadline']
  add_fieldsets = [None, {'fields':['subject','deadline','kredit_reward']}]


  inlines=[SubtaskInLine]

  list_display = ('subject', 'pub_date')

  search_fields = ['subject']

  list_filter=['pub_date']



admin.site.register(Goal, GoalAdmin)
