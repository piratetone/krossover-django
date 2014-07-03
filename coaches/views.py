from django.shortcuts import render
from django.http import Http404

from coaches.models import Coach

def index(request):
  return HttpResponse("Homepage")

def detail(request, coach_id):
  try:
    coach = Coach.objects.get(pk=coach_id)
  except Coach.DoesNotExist:
    raise Http404
  return render(request, 'coaches/detail.html', {'coach' : coach})



