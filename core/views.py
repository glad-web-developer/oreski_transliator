import datetime

from django.shortcuts import render, redirect

# Create your views here.
from core.models import SpisokVosproizvedenia, RaspisaniePoDniam


def render_index(request):
    return render(request, 'index.html', {

    })

def zapolnit_iz_raspisania_na_nedelu(request):
    nomer_dnya_nedeli_segodnia = datetime.datetime.today().isoweekday()
    data_start = datetime.datetime.today() - datetime.timedelta(days=nomer_dnya_nedeli_segodnia)
    data_end = datetime.datetime.today() + datetime.timedelta(days=(7-nomer_dnya_nedeli_segodnia))
    spisok_vozproizvedenia = SpisokVosproizvedenia.objects.filter(data__gte=data_start).filter(data__lte=data_end)
    spisok_vozproizvedenia.delete()

    data_dlia_zapisi = data_start
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
