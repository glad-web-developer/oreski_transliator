import datetime

from django.shortcuts import render

# Create your views here.
from core.models import SpisokVosproizvedenia


def render_index(request):
    return render(request, 'index.html', {

    })

def zapolnit_iz_raspisania_na_nedelu(request):
    nomer_dnya_nedeli_segodnia = datetime.datetime.today().isoweekday()
    data_start = datetime.datetime.today() - datetime.timedelta(days=nomer_dnya_nedeli_segodnia)
    data_end = datetime.datetime.today() + datetime.timedelta(days=(7-nomer_dnya_nedeli_segodnia))
    spisok_vozproizvedenia = SpisokVosproizvedenia.objects.filter(data__gte=data_start).filter(data__lte=data_end)
    spisok_vozproizvedenia.delete()