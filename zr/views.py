from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages as flash_messages

# Create your views here.
def index(req):
    context = {}
    return render(req, 'zr/index.html', context)
