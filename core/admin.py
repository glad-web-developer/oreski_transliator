import datetime

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from core.models import Media, NaborMedia, RaspisaniePoDniam, SpisokVosproizvedenia


class MediaInline(admin.TabularInline):
    model = Media

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        if obj:
            return extra - obj.rn_media.count()
        return extra



class NaborMediaAdmin(ImportExportModelAdmin):

    inlines = [
        MediaInline,
    ]

    list_display = ('id', 'nazvanie', 'recomendovania_prodolzitelnost',  'skorost_perelistivanie_slaida', 'get_spisok_media')
    search_fields = ('nazvanie',)
    # list_filter = ('status_zapisi', 'podriadchik', 'vid_rabot')
    list_display_links = ('id',)

    list_editable = (
        'nazvanie',
        'recomendovania_prodolzitelnost',
        'skorost_perelistivanie_slaida',
    )

    ordering = (['nazvanie',])
    save_on_top = True
    save_as = True


admin.site.register(NaborMedia, NaborMediaAdmin)


class RaspisaniePoDniamAdmin(ImportExportModelAdmin):


    list_display = ('id', 'den_nedeli', 'vremia_s',  'vremia_po',  'nabor_media', 'zvuk')
    # search_fields = ('nazvanie',)
    list_filter = ('den_nedeli', 'nabor_media', )
    list_display_links = ('id',)

    list_editable = (
        'den_nedeli',
        'vremia_s',
        'vremia_po',
        'nabor_media',
        'zvuk',
    )

    ordering = ('den_nedeli','vremia_s')
    save_on_top = True
    save_as = True


admin.site.register(RaspisaniePoDniam, RaspisaniePoDniamAdmin)

@admin.register(SpisokVosproizvedenia)
class SpisokVosproizvedeniaAdmin(ImportExportModelAdmin):
    change_list_template = "model_change_list.html"

    def changelist_view(self, request, extra_context=None):
        result = super(SpisokVosproizvedeniaAdmin, self).changelist_view(request, extra_context)
        # result.context_data['den_seichas'] = datetime.datetime.today().isoweekday()
        return result

    list_display = ('id', 'data', 'vremia_s',  'vremia_po',  'nabor_media', 'zvuk', 'local_id_hash')
    search_fields = ('data',)
    list_filter = ('data', 'nabor_media', )
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
