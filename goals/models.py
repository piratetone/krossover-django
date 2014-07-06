from django.db import models
from django.forms import ModelForm
import datetime

class Goal(models.Model):
  subject = models.CharField(max_length = 200)
  pub_date = models.DateField(auto_now = True)
  kredit_reward = models.IntegerField()
  deadline = models.DateField()

  def __unicode__(self):
    return self.subject  


class SubTask(models.Model):
  goal=models.ForeignKey(Goal)
  task_text = models.CharField(max_length = 1000)

  def __unicode__(self):
    return self.task_text


class GoalForm(ModelForm):
  class Meta:
    model = Goal
    fields = ['subject','kredit_reward','deadline']
