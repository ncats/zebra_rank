from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages as flash_messages

# Create your views here.
def index(req):
    context = {
        'source': 'gard'
    }
    return render(req, 'zr/index.html', context)

def data_source(req, source):
    source = source.lower()
    if source == 'gard' or source == 'orphanet':
        pass
    else:
        context = {
            'message': 'Unknown data source: <b>%s</b>' % source
        }
        return render(req, 'zr/error.html', context)

    context = {
        'source': source
    }
    return render(req, 'zr/index.html', context)
