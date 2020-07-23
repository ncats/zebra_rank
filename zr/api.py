from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
import json, re, sys, logging, traceback
from . import rank_phenotypes as rp

logger = logging.getLogger(__name__)

def index(request):
    return HttpResponse('This is the API for ZebraRank', status=200)

def phenotypes(request, name):
    max = 10
    skip = 0
    if 'skip' in request.GET:
        skip = int(request.GET['skip'])
    if 'max' in request.GET:
        max = int(request.GET['max'])

    name = name.lower()
    matches = []
    for hp in rp.phenotypes.values():
#        print(hp)
        phenotype = hp['name']
        match = None
        if isinstance(phenotype, list):
            for n in phenotype:
                m = n.lower().find(name)
                if m >= 0:
                    match = {
                        'id': hp['id'],
                        'text': n,
                        'pos': m
                    }
                    break
        else:
            m = phenotype.lower().find(name)
            if m >= 0:
                match = {
                    'id': hp['id'],
                    'text': phenotype,
                    'pos': m
                }
            
        if match:
            #logger.debug('matched... %s' % match)
            matches.append(match)
            
    if len(matches) > 0:
        matches = sorted(
            matches, key = lambda x : x['pos']*len(x['text']))[skip:skip+max]

    results = {
        'query': name,
        'results': matches
    }
        
    return HttpResponse(json.dumps(results, indent=2),
                        content_type='application/json', status=200)

@csrf_exempt
def zebra_rank(request):
    phenotypes = []
    if request.method == 'GET':
        if 'phenotypes' in request.GET:
            phenotypes = request.GET['phenotypes'].split(',')
    elif request.method == 'POST':
        try:
            phenotypes = json.loads(request.body)
        except:
            logger.debug("Unexpected error: %s" % sys.exc_info())
            return HttpResponse('Content is not JSON', status=400)
    results = []
    if len(phenotypes) > 0:
        results = rp.rank_phenotypes_weighted_tfidf(phenotypes)
        results = [{'score': r[0],
                    'disease': r[1],
                    'matched_phenotypes': list(r[2])} for r in results]
    return HttpResponse(json.dumps(results, indent=2),
                        content_type='application/json', status=200)
