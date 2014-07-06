from django.shortcuts import render
from django.http import Http404
import datetime

from goals.models import Goal, SubTask

def index(request):
  return HttpResponse("Homepage")

def detail(request, goal_id):
  try:
    goal = Goal.objects.get(pk=goal_id)
  except Goal.DoesNotExist:
    raise Http404
  return render(request, 'goals/detail.html',{'goal':goal})
