from datetime import datetime

from django.db import models
import uuid

class NaborMedia(models.Model):
    class Meta:
        verbose_name = 'Набор медиа'
        verbose_name_plural = 'Набор медиа'

    nazvanie = models.CharField('Название', max_length=250)
    recomendovania_prodolzitelnost = models.CharField('Рекомендованная продолжительность набора', null=True, blank=True, max_length=250)
    skorost_perelistivanie_slaida = models.PositiveIntegerField('Скорость перелистывание слайда в секундах', default=7)


    def get_spisok_media(self):
        tmp = []
        for i in self.rn_media.all():
            tmp.append(i.tip_media)
        return ', '.join(tmp)

    def __str__(self):
        return f'{self.nazvanie} ({self.recomendovania_prodolzitelnost})'


class Media(models.Model):
    class Meta:
        verbose_name = 'Медиа'
        verbose_name_plural = 'Медиа'

    nabor_media = models.ForeignKey(NaborMedia, verbose_name='Набор медиа', on_delete=models.CASCADE, related_name='rn_media')

    tip_media = models.CharField('Тип медиа', max_length=255, choices=(
        ('Видео', 'Видео'),
        ('Аудио', 'Аудио'),
        ('Фото', 'Фото'),
    ))
    media = models.FileField(verbose_name='Файл')

class RaspisaniePoDniam(models.Model):

    class Meta:
        verbose_name='Расписание на неделю'
        verbose_name_plural='Расписание на неделю '

    den_nedeli = models.IntegerField('День недели', choices=(
        (1, 'Понедельник'),
        (2, 'Вторник'),
        (3, 'Среда'),
        (4, 'Четверг'),
        (5, 'Пятница'),
        (6, 'Суббота'),
        (7, 'Воскресенье'),
    ))
    vremia_s = models.TimeField('Время показа с ')
    vremia_po = models.TimeField('Время показа по ')
    nabor_media = models.ForeignKey(NaborMedia, verbose_name='Набор медиа', on_delete=models.CASCADE)
    zvuk = models.BooleanField('Звук', default=True)

    def __str__(self):
        return f'{self.den_nedeli} {self.vremia_s}-{self.vremia_po} {self.nabor_media}'

class SpisokVosproizvedenia(models.Model):

    class Meta:
        verbose_name='Список воспроизведения'
        verbose_name_plural='Список воспроизведения'

    data = models.DateField('Дата')
    vremia_s = models.TimeField('Время показа с ')
    vremia_po = models.TimeField('Время показа по ')
    nabor_media = models.ForeignKey(NaborMedia, verbose_name='Набор медиа', on_delete=models.CASCADE)
    zvuk = models.BooleanField('Звук', default=True)
    local_id_hash = models.CharField(editable=True, blank=True, null=True, max_length=250)

    filtruemoe_dt_s = models.DateTimeField('Фильтрумое дата время с', editable=False)
    filtruemoe_dt_po = models.DateTimeField('Фильтрумое дата время по', editable=False)



    def save(self, *args, **kwargs):
        self.local_id_hash = uuid.uuid4().hex

        self.filtruemoe_dt_s = datetime.combine(self.data, self.vremia_s)
        self.filtruemoe_dt_po = datetime.combine(self.data, self.vremia_po)

        super(SpisokVosproizvedenia, self).save(*args, **kwargs)
