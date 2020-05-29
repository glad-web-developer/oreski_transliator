import datetime
from django.http import HttpResponse

from django.shortcuts import render, redirect

# Create your views here.
from core.models import SpisokVosproizvedenia, RaspisaniePoDniam


def get_hash_igraet_seichas(request):
    try:
        seichas = datetime.datetime.now()
        igraet_seichas = SpisokVosproizvedenia.objects.filter(filtruemoe_dt_s__lte=seichas)
        igraet_seichas = igraet_seichas.filter(filtruemoe_dt_po__gte=seichas)
        igraet_seichas = igraet_seichas[0]
        return HttpResponse(igraet_seichas.local_id_hash)
    except Exception:
        return HttpResponse('-')

def ostanovit_vosproizvedenie(request):
    SpisokVosproizvedenia.objects.all().update(local_id_hash='-')
    return redirect('/admin/core/spisokvosproizvedenia/')

def prodolzit_vosproizvedenie(request):
    for i in SpisokVosproizvedenia.objects.all():
        i.save()
    return redirect('/admin/core/spisokvosproizvedenia/')


def render_index(request):
    seichas = datetime.datetime.now()
    igraet_seichas = SpisokVosproizvedenia.objects.filter(filtruemoe_dt_s__lte=seichas)
    igraet_seichas = igraet_seichas.filter(filtruemoe_dt_po__gte=seichas)
    igraet_seichas = igraet_seichas[0]

    return render(request, 'index.html', {
        'igraet_seichas':igraet_seichas
    })

def zapolnit_iz_raspisania_na_nedelu(request):
    nomer_dnya_nedeli_segodnia = datetime.datetime.today().isoweekday()
    spisok_vozproizvedenia = SpisokVosproizvedenia.objects.all()
    spisok_vozproizvedenia.delete()

    data_dlia_zapisi = datetime.datetime.today() - datetime.timedelta(days=nomer_dnya_nedeli_segodnia-1)

    raspisania_po_dniam = RaspisaniePoDniam.objects.all()

    for nomer_dnia in range(1,8):
        stroki_raspisania_za_den = raspisania_po_dniam.filter(den_nedeli=nomer_dnia)

        for i in stroki_raspisania_za_den:
            SpisokVosproizvedenia(
                data=data_dlia_zapisi,
                vremia_s = i.vremia_s,
                vremia_po = i.vremia_po,
                nabor_media = i.nabor_media,
                zvuk = i.zvuk,
            ).save()

        data_dlia_zapisi = data_dlia_zapisi + datetime.timedelta(days=1)

    return redirect('/admin/core/spisokvosproizvedenia/')

