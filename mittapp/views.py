from django.shortcuts import render
from django.http import HttpResponse, Http404

from django.shortcuts import render

from .models import Achievements

# Create your views here.
def index(request):
    a = Achievements.objects.all()
    return render(request, 'detail.html', {'achievements': a})

