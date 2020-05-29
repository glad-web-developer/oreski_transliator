import datetime

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from core.models import Media, NaborMedia, RaspisaniePoDniam, SpisokVosproizvedenia


class MediaInline(admin.TabularInline):
    model = Media

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        if obj:
            return len(obj.rn_media.all()) - (len(obj.rn_media.all())-1)
        return extra


class NaborMediaAdmin(ImportExportModelAdmin):
    inlines = [
        MediaInline,
    ]

    list_display = (
        'id', 'nazvanie', 'recomendovania_prodolzitelnost', 'skorost_perelistivanie_slaida', 'get_spisok_media')
    search_fields = ('nazvanie',)
    # list_filter = ('status_zapisi', 'podriadchik', 'vid_rabot')
    list_display_links = ('id',)

    list_editable = (
        'nazvanie',
        'recomendovania_prodolzitelnost',
        'skorost_perelistivanie_slaida',
    )

    ordering = (['nazvanie', ])
    save_on_top = True
    save_as = True


admin.site.register(NaborMedia, NaborMediaAdmin)


class RaspisaniePoDniamAdmin(ImportExportModelAdmin):
    list_display = ('id', 'den_nedeli', 'vremia_s', 'vremia_po', 'nabor_media', 'zvuk')
    # search_fields = ('nazvanie',)
    list_filter = ('den_nedeli', 'nabor_media',)
    list_display_links = ('id',)

    list_editable = (
        'den_nedeli',
        'vremia_s',
        'vremia_po',
        'nabor_media',
        'zvuk',
    )

    ordering = ('den_nedeli', 'vremia_s')
    save_on_top = True
    save_as = True


admin.site.register(RaspisaniePoDniam, RaspisaniePoDniamAdmin)


@admin.register(SpisokVosproizvedenia)
class SpisokVosproizvedeniaAdmin(ImportExportModelAdmin):
    change_list_template = "model_change_list.html"

    def get_den_nedeli(self, obj):
        den_nedeli = [
            'Понедельник',
            'Вторник',
            'Среда',
            'Четверг',
            'Пятница',
            'Суббота',
            'Воскресенье',
        ]
        return den_nedeli[obj.data.isoweekday() - 1]

    get_den_nedeli.__name__ = 'День недели'

    def changelist_view(self, request, extra_context=None):
        result = super(SpisokVosproizvedeniaAdmin, self).changelist_view(request, extra_context)
        try:
            seichas = datetime.datetime.now()
            igraet_seichas = SpisokVosproizvedenia.objects.filter(filtruemoe_dt_s__lte=seichas)
            igraet_seichas = igraet_seichas.filter(filtruemoe_dt_po__gte=seichas)
            igraet_seichas = igraet_seichas[0]
            if igraet_seichas.local_id_hash != '-':
                result.context_data['igraet_seichas'] = igraet_seichas.id

        except Exception:
            pass
        return result

    list_display = (
        'id',
        'data',
        'get_den_nedeli',
        'vremia_s',
        'vremia_po',
        'nabor_media',
        'zvuk',
        'local_id_hash',
        'filtruemoe_dt_s',
        'filtruemoe_dt_po',
    )
    search_fields = ('data',)
    list_filter = ('data', 'nabor_media',)
    list_display_links = ('id',)

    list_editable = (
        'data',
        'vremia_s',
        'vremia_po',
        'nabor_media',
        'zvuk',
    )

    ordering = ('data', 'vremia_s')
    save_on_top = True
    save_as = True
